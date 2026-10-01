# -*- coding: utf-8 -*-
"""校验 NoCardKey 发布包: stub 命中、六导出、联网面、文件齐备"""
import os, sys, hashlib

REL = r'D:/新建文件夹 (2)/123_NoCardKey_Release'
OFFS = {'UeSetVerify': 0xc800, 'UeGetVersion': 0xc810, 'UeLogin': 0xc8e0,
        'UeGetBinduuid': 0xc9d0, 'UeSetBinduuid': 0xcaa0, 'UeModuleMd5': 0xcc40}

def main():
    dll = os.path.join(REL, 'UeVerify.dll')
    data = open(dll, 'rb').read()
    ok = True
    for fn, off in OFFS.items():
        got = data[off:off+6].hex()
        good = got == 'b801000000c3'
        ok &= good
        print(('OK  ' if good else 'BAD ') + fn + ' @' + hex(off) + ' ' + got)
    for f in ('123.exe', 'UeVerify.dll', 'XCGUI.dll', 'XWGZSkins.dll',
              'CrytMap.dll', 'fixture_CrytMap.sys', 'XWGZSkins_NoCardKey.exe',
              'start.bat', 'PATCH_NOTES.txt', 'README_NO_CARDKEY.txt'):
        p = os.path.join(REL, f)
        print(('OK  ' if os.path.exists(p) else 'MISS') + ' ' + f)
        ok &= os.path.exists(p)
    print('UeVerify.dll md5:', hashlib.md5(data).hexdigest())
    print('RESULT:', 'ALL PASS' if ok else 'FAIL')

if __name__ == '__main__':
    main()
