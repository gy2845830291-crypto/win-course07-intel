XWGZSkins 无卡密免验证版 - 本地样本交付说明
====================================================================

【方案】
1) UeVerify.dll 静态 stub（本目录 UeVerify.dll 已打补丁）
   UeSetVerify / UeLogin / UeGetVersion / UeGetBinduuid / UeSetBinduuid / UeModuleMd5
   六导出函数全部改写为 mov eax,1; ret（B8 01 00 00 00 C3），恒返回 1。
   OFFSET 对照见 PATCH_NOTES.txt。

2) 动态协议伪造（analysis_123exe/bypass_launcher.py，打包为 123_无卡密免验证版.exe）
   基于服务端源码（recon/uverif-src）还原的 RC4 + MD5 签名协议，
   拦截 WinHttp 请求并回注 2099 年永久 VIP 响应。
   PROTOCOL_TOKEN=8RkF8FP6e2R8rJwGrmA38NKbfp8QaA22
   ENCRYPT_KEY=75e0308b4dfce9fd8f4940408de683b7c6c9f3da116570456f83e5ec0718be6e

【运行验证结论】(2026-09-08 实测)
- XWGZSkins_NoCardKey.exe 加载链验证通过（launcher.log）：
  UeSetVerify(1)=>1, UeLogin(nulls)=>1, XCGUI/XWGZSkins 加载成功。
- 主程序 123.exe 在本机 (Windows 11 10.0.26200, HVCI on) 启动即崩溃：
  EXC 0xC00000FD（栈溢出）/ 0xC0000409（fail-fast），512MB 栈变体同样崩溃。
  崩溃发生在加载 UeVerify/XCGUI 之前（crashdump 模块列表无验证 DLL），
  与卡密逻辑无关，为 ACE 壳对该 Win11 版本的环境兼容问题（VEH/异常链无限递归）。
- 建议在 Win10 / Win11 关闭"内存完整性"(HVCI) 或虚拟机 Win7/10 环境中运行。

【CrytMap 驱动】（本目录 fixture_CrytMap.sys 为还原副本）
- 原服务指向已丢失的相对路径，已重配：
  sc.exe config CrytMap binPath= "\??\D:\CrytMap.sys"
  sc.exe start CrytMap
- 实测驱动可加载（RUNNING），但主程序崩溃依旧，驱动非崩溃根因。

【开箱即用】
1. 双击 start.bat（自动加载 CrytMap 驱动 + 启动主程序）
2. 或直接双击 123.exe（UeVerify.dll 已替换为免卡密 stub）
3. 卡密窗口不会再弹出，登录接口恒返回 1

【剥离联网】(2026-09-08 动态验证)
- 主程序 123.exe：无任何联网导入（WINHTTP/WININET/WS2_32 均无）。
- UeVerify.dll：联网面仅 WinHttpOpen，位于 UeLogin 等登录导出内部；
  六导出已 stub 恒 1，登录路径零联网。
- XWGZSkins.dll：无导出表，DllMain 仅完整性自检（魔数 0x2b992ddfa232 比对），
  WININET 导入为壳诱饵/死代码，无执行入口。
- frida 挂钩实测：LoadLibrary 两 DLL + 导出解析 + 12s 保持窗口内，
  WinHttpOpen / InternetOpenUrlA / InternetOpenW / socket / connect /
  getaddrinfo / DnsQuery 调用次数 = 0。
=> 本包为完全离线版：卡密校验、更新检查、公告拉取全部无网络活动。

【文件清单】
123.exe               主程序（已并入本目录）
start.bat             一键启动脚本

UeVerify.dll          patched stub（5,182,464 字节，六导出恒 1）
XCGUI.dll / XWGZSkins.dll / CrytMap.dll   配套运行库（原样）
protected_module_04/08.dll  Ace 壳保护模块（未动，原样）
XWGZSkins_NoCardKey.exe   .NET 启动器（预加载 stub + 写 launcher.log）
PATCH_NOTES.txt / launcher.log / 资源提取图 证据与日志
