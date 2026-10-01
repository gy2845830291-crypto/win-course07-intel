# -*- coding: utf-8 -*-
"""
XWGZSkins 新版自动重破 + 剥离联网工具
用法:
  python update_patch.py <新版123.exe或新版目录> [输出目录]

流程:
  1) 在新版目录定位 UeVerify.dll（exe 同目录优先）
  2) pefile 解析六导出 RVA -> 文件偏移
  3) 备份原 DLL -> UeVerify_orig.dll，在偏移处写 B8 01 00 00 00 C3
  4) 更新 PATCH_NOTES.txt（旧字节/新偏移）
  5) 静态核验: 联网导入（WINHTTP/WININET/WS2_32/URLMON）调用面为零
输出: 与 123_NoCardKey_Release 同构的离线发布目录
"""
import sys, os, shutil, hashlib, struct, re

TARGET_EXPORTS = ['UeSetVerify', 'UeLogin', 'UeGetVersion',
                  'UeGetBinduuid', 'UeSetBinduuid', 'UeModuleMd5']
PATCH = bytes.fromhex('b801000000c3')  # mov eax,1; ret
NET_DLLS = ('winhttp', 'wininet', 'ws2_32', 'urlmon', 'dnsapi')

def find_ueverify(exe_or_dir):
    if os.path.isfile(exe_or_dir):
        cand = os.path.join(os.path.dirname(os.path.abspath(exe_or_dir)), 'UeVerify.dll')
        return cand if os.path.exists(cand) else None
    cand = os.path.join(exe_or_dir, 'UeVerify.dll')
    return cand if os.path.exists(cand) else None

def rva_to_offset(pe, rva):
    for s in pe.sections:
        va, vs, rs, rd = s.VirtualAddress, s.Misc_VirtualSize, s.PointerToRawData, s.SizeOfRawData
        if va <= rva < va + max(vs, rd):
            return rs + (rva - va)
    return None

def patch_dll(dll_path):
    import pefile
    pe = pefile.PE(dll_path)
    exp = pe.DIRECTORY_ENTRY_EXPORT
    table = {}
    for s in exp.symbols:
        if s.name:
            table[s.name.decode()] = s.address
    missing = [e for e in TARGET_EXPORTS if e not in table]
    if missing:
        raise SystemExit('导出缺失: ' + ', '.join(missing))
    raw = bytearray(open(dll_path, 'rb').read())
    notes = []
    for fn in TARGET_EXPORTS:
        rva = table[fn]
        off = rva_to_offset(pe, rva)
        if off is None:
            raise SystemExit(fn + ' RVA 无映射')
        old = bytes(raw[off:off+6])
        raw[off:off+6] = PATCH
        notes.append((fn, rva, off, old.hex(), 'b801000000c3'))
    return notes, table, bytes(raw)

def net_audit(dll_path):
    import pefile
    pe = pefile.PE(dll_path)
    net = []
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for e in pe.DIRECTORY_ENTRY_IMPORT:
            d = e.dll.decode().lower()
            if any(k in d for k in NET_DLLS):
                net.append((e.dll.decode(), [i.name.decode() if i.name else 'ord%d' % i.ordinal for i in e.imports]))
    return net

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else '.'
    out = sys.argv[2] if len(sys.argv) > 2 else 'NoCardKey_Offline_Release'
    dll = find_ueverify(src)
    if not dll:
        raise SystemExit('未找到 UeVerify.dll，请给新版 123.exe 路径或新版目录')
    notes, table, patched = patch_dll(dll)
    net = net_audit(dll)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'UeVerify.dll'), 'wb') as f:
        f.write(patched)
    shutil.copy2(dll, os.path.join(out, 'UeVerify_orig.dll'))
    if os.path.isfile(os.path.join(os.path.dirname(dll), '123.exe')):
        shutil.copy2(os.path.join(os.path.dirname(dll), '123.exe'), os.path.join(out, '123.exe'))
    for f in ('XCGUI.dll', 'XWGZSkins.dll', 'CrytMap.dll', 'fixture_CrytMap.sys'):
        p = os.path.join(os.path.dirname(dll), f)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(out, f))
    with open(os.path.join(out, 'PATCH_NOTES.txt'), 'w', encoding='utf-8') as f:
        f.write('# auto regen ' + __import__('datetime').datetime.now().isoformat(timespec='seconds') + '\n')
        for fn, rva, off, old, new in notes:
            f.write('CHECK_FN=%s RVA=%#x OFFSET=%#x OLD=%s NEW=%s\n' % (fn, rva, off, old, new))
        f.write('NET_IMPORTS=%s\n' % (net if net else 'NONE'))
    h = hashlib.md5(patched).hexdigest()
    print('OK 输出目录:', os.path.abspath(out))
    print('UeVerify.dll md5:', h)
    print('导出 patch:')
    for fn, rva, off, old, new in notes:
        print('  %-16s RVA=%#x OFFSET=%#x %s -> %s' % (fn, rva, off, old, new))
    print('联网导入面:', net if net else 'NONE (离线)')

if __name__ == '__main__':
    main()
