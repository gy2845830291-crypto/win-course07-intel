import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def relaunch_as_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(f'"{a}"' for a in sys.argv), None, 1)
        sys.exit(0)
    except Exception:
        pass

if not is_admin():
    relaunch_as_admin()

import os, sys, time, json, hashlib, frida

CLIENT_TAG = "clientlogin"
UDID_SUFFIX = "-648f38eb"
PROTOCOL_TOKEN = "8RkF8FP6e2R8rJwGrmA38NKbfp8QaA22"

def md5hex(data: str) -> str:
    return hashlib.md5(data.encode("utf-8")).hexdigest()

def rc4(key: bytes, data: bytes) -> bytes:
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) & 0xff
        s[i], s[j] = s[j], s[i]
    i = j = 0
    out = bytearray()
    for b in data:
        i = (i + 1) & 0xff
        j = (j + s[i]) & 0xff
        s[i], s[j] = s[j], s[i]
        out.append(b ^ s[(s[i] + s[j]) & 0xff])
    return bytes(out)

def generate_valid_response(user: str, udid: str, timestamp: int):
    bucket = str(timestamp)[:8]
    outer_sign = md5hex(bucket + user + udid).lower()
    
    vip_exp_time = 4102444799 # 2099-12-31 23:59:59
    vip_exp_date = "2099-12-31"
    
    inner_raw = f"{user}{vip_exp_date}{vip_exp_time}{timestamp}{udid}"
    inner_sign = md5hex(inner_raw).upper()
    
    plain_dict = {
        "time": timestamp,
        "code": 1,
        "vipExpTime": vip_exp_time,
        "vipExpDate": vip_exp_date,
        "state": 1,
        "user": user,
        "udid": udid,
        "sign": inner_sign
    }
    plain_json = json.dumps(plain_dict, separators=(',', ':'))
    rc4_key = md5hex(user + PROTOCOL_TOKEN + udid).lower().encode('ascii')
    encrypted_data_hex = rc4(rc4_key, plain_json.encode('utf-8')).hex()
    
    resp = {
        "code": 200,
        "msg": "ok",
        "time": timestamp,
        "data": {
            "sign": outer_sign,
            "state": 1,
            "vipExpTime": vip_exp_time,
            "vipExpDate": vip_exp_date,
            "data": encrypted_data_hex
        }
    }
    return json.dumps(resp, separators=(',', ':'))

JS_HOOK = r"""
var reqTime = null;
var reqUser = "VIP_USER";
var reqUdid = "812EE57436413E3367D60011F4058B9B";

function parseBuffer(buf, len) {
    try {
        var s = buf.readCString(Math.min(len, 1024));
        if (!s) return;
        var mTime = /time=(\d{10})/.exec(s);
        if (mTime) reqTime = parseInt(mTime[1], 10);
        var mUser = /user=([^&]+)/.exec(s);
        if (mUser) reqUser = decodeURIComponent(mUser[1]);
        var mUdid = /udid=([^&]+)/.exec(s);
        if (mUdid) reqUdid = decodeURIComponent(mUdid[1]);
    } catch(e) {}
}

var modWinHttp = Process.findModuleByName("winhttp.dll");
if (modWinHttp) {
    var pWrite = modWinHttp.findExportByName("WinHttpWriteData");
    if (pWrite) {
        Interceptor.attach(pWrite, {
            onEnter: function(args) {
                parseBuffer(args[1], args[2].toUInt32());
            }
        });
    }
    var pSend = modWinHttp.findExportByName("WinHttpSendRequest");
    if (pSend) {
        Interceptor.attach(pSend, {
            onEnter: function(args) {
                var len = args[5].toUInt32();
                if (len > 0 && !args[4].isNull()) {
                    parseBuffer(args[4], len);
                }
            }
        });
    }
    var pRead = modWinHttp.findExportByName("WinHttpReadData");
    if (pRead) {
        Interceptor.attach(pRead, {
            onEnter: function(args) {
                this.buf = args[1];
                this.pReadLen = args[3];
            },
            onLeave: function(retval) {
                var readLen = this.pReadLen.readU32();
                if (readLen > 0) {
                    var nowTs = reqTime ? reqTime : Math.floor(Date.now() / 1000);
                    send({
                        type: "request_detected",
                        user: reqUser,
                        udid: reqUdid,
                        time: nowTs
                    });
                    var op = recv('make_response', function(val) {
                        var body = val.body;
                        Memory.writeUtf8String(this.buf, body);
                        this.pReadLen.writeU32(body.length);
                    });
                    op.wait();
                }
            }
        });
    }
}
"""

def main():
    target_exe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "123.exe")
    if not os.path.exists(target_exe):
        target_exe = r"D:\新建文件夹 (2)\analysis_123exe\123.exe"
    
    print("[*] 正在以无卡密免验证模式启动目标程序:", target_exe)
    device = frida.get_local_device()
    pid = device.spawn([target_exe])
    session = device.attach(pid)
    
    script = session.create_script(JS_HOOK)
    
    def on_message(message, data):
        if message.get('type') == 'send':
            payload = message.get('payload', {})
            if payload.get('type') == 'request_detected':
                u = payload.get('user', 'VIP_USER')
                ud = payload.get('udid', '812EE57436413E3367D60011F4058B9B')
                t = payload.get('time', int(time.time()))
                print(f"[+] 捕获卡密请求: 用户={u}, UDID={ud}, 时间戳={t}")
                body = generate_valid_response(u, ud, t)
                print("[+] 已成功注入 2099 年永久 VIP 授权数据包！")
                script.post({'type': 'make_response', 'body': body})
    
    script.on('message', on_message)
    script.load()
    device.resume(pid)
    print("[+] 目标程序主线程已恢复，拦截守护运行中，双击或直接点击登录即可免卡密使用！")
    
    # 保持守护直到目标进程退出
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
