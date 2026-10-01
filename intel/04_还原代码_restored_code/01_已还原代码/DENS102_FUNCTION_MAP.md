# dens102 loader-valid PE function map

- Input: `SAMPLE_dens102_hist_h4000_text_denser_asInvoker.exe`
- `.text` runtime functions: **1165**
- Resolved IAT slots: **104**
- Functions changed from the dens101 hollows image: **367**
- Validation: `SEC_IMAGE` + `CreateProcess(CREATE_SUSPENDED)`; primary thread was never resumed.

## Most referenced imported APIs

- `kernel32.dll!GetLastError`: 28
- `kernel32.dll!CloseHandle`: 13
- `kernel32.dll!WriteFile`: 7
- `kernel32.dll!SetLastError`: 7
- `kernel32.dll!GetProcAddress`: 6
- `kernel32.dll!CreateFileW`: 6
- `kernel32.dll!DeleteCriticalSection`: 6
- `kernel32.dll!AcquireSRWLockExclusive`: 5
- `kernel32.dll!GetModuleHandleW`: 4
- `kernel32.dll!ReadFile`: 4
- `kernel32.dll!ReleaseSRWLockExclusive`: 4
- `kernel32.dll!IsProcessorFeaturePresent`: 4
- `kernel32.dll!RtlLookupFunctionEntry`: 4
- `kernel32.dll!RaiseException`: 4
- `kernel32.dll!LoadLibraryExW`: 4
- `kernel32.dll!FreeLibrary`: 4
- `kernel32.dll!GetModuleHandleA`: 3
- `kernel32.dll!SetFilePointerEx`: 3
- `kernel32.dll!IsDebuggerPresent`: 3
- `kernel32.dll!SetUnhandledExceptionFilter`: 3
- `kernel32.dll!UnhandledExceptionFilter`: 3
- `kernel32.dll!GetCurrentProcess`: 3
- `kernel32.dll!RtlCaptureContext`: 3
- `kernel32.dll!RtlVirtualUnwind`: 3
- `kernel32.dll!RtlUnwindEx`: 3
- `kernel32.dll!GetFileType`: 3
- `kernel32.dll!VirtualProtect`: 3
- `kernel32.dll!MultiByteToWideChar`: 2
- `kernel32.dll!GetFileSizeEx`: 2
- `kernel32.dll!GetCurrentThreadId`: 2

## Newly recovered `.text` functions

- `0x77e0`–`0xb7e8` size `0x4008`; changed `15929` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x1a6ff`–`0x1ddad` size `0x36ae`; changed `13630` bytes; base nonzero `0`; APIs: kernel32.dll!GetModuleHandleA×1
- `0x12c40`–`0x15f24` size `0x32e4`; changed `12634` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x3a40`–`0x72a9` size `0x3869`; changed `12552` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xfde0`–`0x12477` size `0x2697`; changed `9339` bytes; base nonzero `0`; APIs: user32.dll!LoadCursorW×1
- `0xd8a0`–`0xfdd3` size `0x2533`; changed `9189` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x15f30`–`0x178b7` size `0x1987`; changed `6357` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2505e`–`0x25a50` size `0x9f2`; changed `2500` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x1fac0`–`0x203b8` size `0x8f8`; changed `2279` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x29347`–`0x29b44` size `0x7fd`; changed `1876` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x23050`–`0x2379a` size `0x74a`; changed `1728` bytes; base nonzero `0`; APIs: kernel32.dll!CloseHandle×2
- `0x2d4c0`–`0x2dbd8` size `0x718`; changed `1679` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2a970`–`0x2b056` size `0x6e6`; changed `1527` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xca40`–`0xd199` size `0x759`; changed `1512` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x28240`–`0x28890` size `0x650`; changed `1461` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x27b18`–`0x28172` size `0x65a`; changed `1455` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2741b`–`0x27a5d` size `0x642`; changed `1448` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x25d60`–`0x262ab` size `0x54b`; changed `1355` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x28978`–`0x28f4c` size `0x5d4`; changed `1350` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x181a0`–`0x186f6` size `0x556`; changed `1231` bytes; base nonzero `0`; APIs: kernel32.dll!CloseHandle×2
- `0x1ebe0`–`0x1f0ec` size `0x50c`; changed `1197` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x21470`–`0x2187c` size `0x40c`; changed `941` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2b8e0`–`0x2bc7d` size `0x39d`; changed `854` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2ca02`–`0x2cdf2` size `0x3f0`; changed `850` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x18900`–`0x18ca5` size `0x3a5`; changed `840` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x19950`–`0x19ca7` size `0x357`; changed `838` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x7400`–`0x7762` size `0x362`; changed `804` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2a5d0`–`0x2a969` size `0x399`; changed `738` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x21880`–`0x21bc6` size `0x346`; changed `727` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x19630`–`0x1994b` size `0x31b`; changed `723` bytes; base nonzero `0`; APIs: kernel32.dll!CloseHandle×1
- `0x2a2a0`–`0x2a5c1` size `0x321`; changed `718` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xd590`–`0xd899` size `0x309`; changed `716` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x1f330`–`0x1f622` size `0x2f2`; changed `696` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x1f630`–`0x1f911` size `0x2e1`; changed `677` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x26d83`–`0x27012` size `0x28f`; changed `635` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x237f0`–`0x23ac8` size `0x2d8`; changed `630` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x20fa6`–`0x2124c` size `0x2a6`; changed `617` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x18ca5`–`0x18f40` size `0x29b`; changed `603` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x22100`–`0x22372` size `0x272`; changed `564` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2b130`–`0x2b36f` size `0x23f`; changed `525` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x19323`–`0x1956b` size `0x248`; changed `519` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x19cb0`–`0x19ef6` size `0x246`; changed `518` bytes; base nonzero `0`; APIs: kernel32.dll!K32GetModuleFileNameExW×1
- `0x28f6e`–`0x29193` size `0x225`; changed `514` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x26b94`–`0x26d83` size `0x1ef`; changed `470` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2c332`–`0x2c569` size `0x237`; changed `466` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x20d76`–`0x20f86` size `0x210`; changed `463` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x21ef0`–`0x220f1` size `0x201`; changed `462` bytes; base nonzero `0`; APIs: kernel32.dll!GetModuleHandleA×1, kernel32.dll!GetProcAddress×1, kernel32.dll!LoadLibraryA×1
- `0x19040`–`0x1924d` size `0x20d`; changed `459` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x25b80`–`0x25d5f` size `0x1df`; changed `457` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x18700`–`0x188f9` size `0x1f9`; changed `451` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x29ef4`–`0x2a0ea` size `0x1f6`; changed `446` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2c730`–`0x2c91a` size `0x1ea`; changed `445` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x224f0`–`0x226cf` size `0x1df`; changed `443` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x26910`–`0x26ade` size `0x1ce`; changed `437` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2124c`–`0x2143c` size `0x1f0`; changed `436` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x17e20`–`0x18005` size `0x1e5`; changed `436` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x24377`–`0x24541` size `0x1ca`; changed `434` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x24587`–`0x24751` size `0x1ca`; changed `434` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x27020`–`0x271e0` size `0x1c0`; changed `430` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2bc80`–`0x2be54` size `0x1d4`; changed `410` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x22750`–`0x228ff` size `0x1af`; changed `393` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2c569`–`0x2c72c` size `0x1c3`; changed `387` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x17a70`–`0x17c0b` size `0x19b`; changed `386` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xd400`–`0xd587` size `0x187`; changed `372` bytes; base nonzero `0`; APIs: kernel32.dll!MultiByteToWideChar×2
- `0x2cfcd`–`0x2d17c` size `0x1af`; changed `370` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xd230`–`0xd3d1` size `0x1a1`; changed `364` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x124c0`–`0x12637` size `0x177`; changed `364` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x271e0`–`0x27353` size `0x173`; changed `349` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2d17c`–`0x2d302` size `0x186`; changed `337` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xbf20`–`0xc080` size `0x160`; changed `333` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x22380`–`0x224ec` size `0x16c`; changed `331` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0xc260`–`0xc3ae` size `0x14e`; changed `314` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x2668a`–`0x267d3` size `0x149`; changed `314` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x72b0`–`0x73fa` size `0x14a`; changed `311` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x24780`–`0x248d9` size `0x159`; changed `308` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x17cc0`–`0x17e16` size `0x156`; changed `308` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x20628`–`0x2075f` size `0x137`; changed `308` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x204e6`–`0x20628` size `0x142`; changed `304` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x264da`–`0x2660b` size `0x131`; changed `304` bytes; base nonzero `0`; APIs: (no direct IAT calls)
- `0x20ae0`–`0x20c2e` size `0x14e`; changed `303` bytes; base nonzero `0`; APIs: (no direct IAT calls)

## Highest-signal functions

### RVA `0x55268`–`0x5567b` (0x413)
- Decode ratio: `1.0`; instructions: `282`
- Imports: kernel32.dll!CloseHandle×2, kernel32.dll!CreateFileW×3, kernel32.dll!GetFileType×1, kernel32.dll!GetLastError×3
- Direct in-image targets: 0x49490, 0x494dc, 0x49500, 0x4f1c4, 0x52c08, 0x52cf0, 0x52e30, 0x54d10, 0x54f90, 0x551a4, 0x552e7, 0x55497, 0x554fe, 0x5565a

### RVA `0x4f3e8`–`0x4f59a` (0x1b2)
- Decode ratio: `1.0`; instructions: `114`
- Imports: kernel32.dll!FreeLibrary×1, kernel32.dll!GetLastError×1, kernel32.dll!GetProcAddress×1, kernel32.dll!LoadLibraryExW×2, kernel32.dll!VirtualProtect×2
- Direct in-image targets: 0x49558, 0x49b18, 0x49b6c, 0x4b530, 0x4f4cb, 0x4f4da

### RVA `0x3dcbc`–`0x3de04` (0x148)
- Decode ratio: `1.0`; instructions: `71`
- Imports: kernel32.dll!IsDebuggerPresent×1, kernel32.dll!IsProcessorFeaturePresent×1, kernel32.dll!RtlCaptureContext×1, kernel32.dll!RtlLookupFunctionEntry×1, kernel32.dll!RtlVirtualUnwind×1, kernel32.dll!SetUnhandledExceptionFilter×1, kernel32.dll!UnhandledExceptionFilter×1
- Direct in-image targets: 0x3dcb4, 0x57920

### RVA `0x43118`–`0x43285` (0x16d)
- Decode ratio: `1.0`; instructions: `86`
- Imports: kernel32.dll!IsDebuggerPresent×1, kernel32.dll!RtlCaptureContext×1, kernel32.dll!RtlLookupFunctionEntry×1, kernel32.dll!RtlVirtualUnwind×1, kernel32.dll!SetUnhandledExceptionFilter×1, kernel32.dll!UnhandledExceptionFilter×1
- Direct in-image targets: 0x3cfb0, 0x3dcb4, 0x57920

### RVA `0x4286c`–`0x429bb` (0x14f)
- Decode ratio: `1.0`; instructions: `88`
- Imports: kernel32.dll!FreeLibrary×1, kernel32.dll!GetLastError×1, kernel32.dll!GetProcAddress×1, kernel32.dll!LoadLibraryExW×2
- Direct in-image targets: 0x42949, 0x42960, 0x4b530

### RVA `0x4fe80`–`0x502df` (0x45f)
- Decode ratio: `1.0`; instructions: `293`
- Imports: kernel32.dll!GetConsoleMode×1, kernel32.dll!GetLastError×2, kernel32.dll!ReadConsoleW×1, kernel32.dll!ReadFile×1
- Direct in-image targets: 0x433e4, 0x49490, 0x494dc, 0x49500, 0x4bc20, 0x4bc80, 0x4f954, 0x4fb50, 0x5001c, 0x5012f, 0x50132, 0x50194, 0x501d6, 0x5022f, 0x50254, 0x502bf, 0x502c4, 0x502c7, 0x5054c, 0x54bac

### RVA `0x5665c`–`0x5671a` (0xbe)
- Decode ratio: `1.0`; instructions: `48`
- Imports: kernel32.dll!CloseHandle×1, kernel32.dll!CreateFileW×1, kernel32.dll!GetLastError×1, kernel32.dll!WriteConsoleW×2
- Direct in-image targets: (none)

### RVA `0x3c420`–`0x3c551` (0x131)
- Decode ratio: `1.0`; instructions: `92`
- Imports: kernel32.dll!AcquireSRWLockExclusive×2, kernel32.dll!GetCurrentThreadId×1, kernel32.dll!TryAcquireSRWLockExclusive×2
- Direct in-image targets: 0x3c4a0, 0x3c4ed, 0x3c52d, 0x3c52f, 0x3c59c, 0x3cfb0

### RVA `0x4e858`–`0x4eb87` (0x32f)
- Decode ratio: `1.0`; instructions: `229`
- Imports: kernel32.dll!GetConsoleMode×1, kernel32.dll!GetLastError×2, kernel32.dll!WriteFile×1
- Direct in-image targets: 0x4332c, 0x47750, 0x494b8, 0x4de74, 0x4e308, 0x4e410, 0x4e52c, 0x4e8b7, 0x4ea2d, 0x4eae4, 0x4eae9, 0x4eb76, 0x505e8, 0x54bac, 0x54c0c

### RVA `0x4de74`–`0x4e307` (0x493)
- Decode ratio: `1.0`; instructions: `304`
- Imports: kernel32.dll!GetConsoleOutputCP×1, kernel32.dll!GetLastError×1, kernel32.dll!WriteFile×2
- Direct in-image targets: 0x3cfb0, 0x47750, 0x4cc88, 0x4d0e4, 0x4df3d, 0x4e167, 0x4e17c, 0x4e2dd, 0x50ed4, 0x57270

### RVA `0x3d6dc`–`0x3d710` (0x34)
- Decode ratio: `1.0`; instructions: `13`
- Imports: kernel32.dll!GetCurrentProcess×1, kernel32.dll!SetUnhandledExceptionFilter×1, kernel32.dll!TerminateProcess×1, kernel32.dll!UnhandledExceptionFilter×1
- Direct in-image targets: (none)

### RVA `0x51680`–`0x51a7d` (0x3fd)
- Decode ratio: `1.0`; instructions: `283`
- Imports: kernel32.dll!FindClose×2, kernel32.dll!FindFirstFileExW×1, kernel32.dll!FindNextFileW×1
- Direct in-image targets: 0x3cfb0, 0x433e4, 0x43434, 0x49500, 0x4a6d8, 0x4bc20, 0x516f6, 0x518b7, 0x5198e, 0x51a40, 0x51a80, 0x52944, 0x53230, 0x55a60, 0x57920

### RVA `0x3df0c`–`0x3dfb8` (0xac)
- Decode ratio: `1.0`; instructions: `39`
- Imports: kernel32.dll!GetCurrentProcessId×1, kernel32.dll!GetCurrentThreadId×1, kernel32.dll!GetSystemTimeAsFileTime×1, kernel32.dll!QueryPerformanceCounter×1
- Direct in-image targets: (none)

### RVA `0x43434`–`0x4347b` (0x47)
- Decode ratio: `1.0`; instructions: `20`
- Imports: kernel32.dll!GetCurrentProcess×1, kernel32.dll!IsProcessorFeaturePresent×1, kernel32.dll!TerminateProcess×1
- Direct in-image targets: 0x43118

### RVA `0x4b86c`–`0x4b921` (0xb5)
- Decode ratio: `1.0`; instructions: `51`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×2
- Direct in-image targets: 0x4b684, 0x4b898, 0x4b906, 0x4b911, 0x4bc20, 0x4f370, 0x4f61c

### RVA `0x4a454`–`0x4a4b8` (0x64)
- Decode ratio: `1.0`; instructions: `26`
- Imports: kernel32.dll!FreeLibrary×1, kernel32.dll!GetModuleHandleExW×1, kernel32.dll!GetProcAddress×1
- Direct in-image targets: 0x57150

### RVA `0x3d078`–`0x3d0f0` (0x78)
- Decode ratio: `1.0`; instructions: `27`
- Imports: KERNELBASE.dll!SleepConditionVariableSRW×1, kernel32.dll!AcquireSRWLockExclusive×1, kernel32.dll!ReleaseSRWLockExclusive×1
- Direct in-image targets: 0x3d08e, 0x3d0dd

### RVA `0x3d7e4`–`0x3d855` (0x71)
- Decode ratio: `1.0`; instructions: `33`
- Imports: kernel32.dll!RtlCaptureContext×1, kernel32.dll!RtlLookupFunctionEntry×1, kernel32.dll!RtlVirtualUnwind×1
- Direct in-image targets: (none)

### RVA `0x3d00c`–`0x3d075` (0x69)
- Decode ratio: `1.0`; instructions: `21`
- Imports: kernel32.dll!AcquireSRWLockExclusive×1, kernel32.dll!ReleaseSRWLockExclusive×1, kernel32.dll!WakeAllConditionVariable×1
- Direct in-image targets: (none)

### RVA `0x3cfd0`–`0x3d009` (0x39)
- Decode ratio: `1.0`; instructions: `12`
- Imports: kernel32.dll!AcquireSRWLockExclusive×1, kernel32.dll!ReleaseSRWLockExclusive×1, kernel32.dll!WakeAllConditionVariable×1
- Direct in-image targets: (none)

### RVA `0x21ef0`–`0x220f1` (0x201)
- Decode ratio: `1.0`; instructions: `138`
- Imports: kernel32.dll!GetModuleHandleA×1, kernel32.dll!GetProcAddress×1, kernel32.dll!LoadLibraryA×1
- Direct in-image targets: 0x21fda, 0x21fdc

### RVA `0x3ceb4`–`0x3cf59` (0xa5)
- Decode ratio: `1.0`; instructions: `42`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!IsDebuggerPresent×1, kernel32.dll!OutputDebugStringW×1
- Direct in-image targets: 0x1c60, 0x57920

### RVA `0x3ce28`–`0x3ce74` (0x4c)
- Decode ratio: `1.0`; instructions: `17`
- Imports: kernel32.dll!GetModuleHandleW×1, kernel32.dll!GetProcAddress×2
- Direct in-image targets: (none)

### RVA `0x4bc20`–`0x4bc5c` (0x3c)
- Decode ratio: `1.0`; instructions: `19`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!HeapFree×1
- Direct in-image targets: 0x493c0, 0x49500

### RVA `0x42ff8`–`0x4305f` (0x67)
- Decode ratio: `1.0`; instructions: `30`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×1
- Direct in-image targets: 0x4302c, 0x49558, 0x4ba7c

### RVA `0x3f390`–`0x3f437` (0xa7)
- Decode ratio: `1.0`; instructions: `44`
- Imports: kernel32.dll!RaiseException×1, kernel32.dll!RtlPcToFileHeader×1
- Direct in-image targets: (none)

### RVA `0x4b9ec`–`0x4ba7c` (0x90)
- Decode ratio: `1.0`; instructions: `43`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×1
- Direct in-image targets: 0x4b86c, 0x4ba20, 0x4ba53, 0x4ba6e, 0x4f608, 0x4f610

### RVA `0x4f25c`–`0x4f329` (0xcd)
- Decode ratio: `1.0`; instructions: `59`
- Imports: kernel32.dll!CloseHandle×1, kernel32.dll!GetLastError×1
- Direct in-image targets: 0x494b8, 0x4f2dc, 0x4f319, 0x52e30, 0x52eec

### RVA `0x50400`–`0x504af` (0xaf)
- Decode ratio: `1.0`; instructions: `47`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetFilePointerEx×1
- Direct in-image targets: 0x494b8, 0x50438, 0x5049a, 0x52eec

### RVA `0x51de0`–`0x51e5d` (0x7d)
- Decode ratio: `1.0`; instructions: `31`
- Imports: kernel32.dll!GetACP×1, kernel32.dll!GetOEMCP×1
- Direct in-image targets: 0x42c78, 0x51e27, 0x51e42

### RVA `0x4fb50`–`0x4fe7f` (0x32f)
- Decode ratio: `1.0`; instructions: `232`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!ReadFile×1
- Direct in-image targets: 0x49490, 0x49500, 0x4fba9, 0x4fbee, 0x4fcb9, 0x4fcbc, 0x4fd0e, 0x4fd37, 0x4fdec, 0x4fe67, 0x5054c, 0x514dc

### RVA `0x52494`–`0x5275c` (0x2c8)
- Decode ratio: `1.0`; instructions: `197`
- Imports: kernel32.dll!GetCPInfo×1, kernel32.dll!IsValidCodePage×1
- Direct in-image targets: 0x3cfb0, 0x51de0, 0x51e60, 0x51ef8, 0x52538, 0x52612, 0x5261d, 0x526fa, 0x52722, 0x52734, 0x52736, 0x57920

### RVA `0x567b4`–`0x56942` (0x18e)
- Decode ratio: `1.0`; instructions: `116`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetEndOfFile×1
- Direct in-image targets: 0x4b27c, 0x4bc20, 0x4e858, 0x4f370, 0x5054c, 0x52eec, 0x568a5, 0x56909, 0x56913

### RVA `0xd400`–`0xd587` (0x187)
- Decode ratio: `1.0`; instructions: `117`
- Imports: kernel32.dll!MultiByteToWideChar×2
- Direct in-image targets: 0x1c70, 0x2560, 0x2570, 0xba20, 0xc4c0, 0xd504, 0xd53a, 0x12790, 0x127c0, 0x3cfb0, 0x57920

### RVA `0x4e52c`–`0x4e6a0` (0x174)
- Decode ratio: `1.0`; instructions: `100`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!WriteFile×1
- Direct in-image targets: 0x3cfb0, 0x3dc30, 0x4e671, 0x50ed4

### RVA `0x52cf0`–`0x52e2e` (0x13e)
- Decode ratio: `1.0`; instructions: `83`
- Imports: kernel32.dll!EnterCriticalSection×1, kernel32.dll!LeaveCriticalSection×1
- Direct in-image targets: 0x49b18, 0x49b6c, 0x52a40, 0x52be0, 0x52d20, 0x52d85, 0x52daa, 0x52e07

### RVA `0x4e410`–`0x4e52b` (0x11b)
- Decode ratio: `1.0`; instructions: `77`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!WriteFile×1
- Direct in-image targets: 0x3cfb0, 0x3dc30, 0x4e500

### RVA `0x4d530`–`0x4d638` (0x108)
- Decode ratio: `1.0`; instructions: `71`
- Imports: kernel32.dll!GetFileType×1, kernel32.dll!GetStdHandle×1
- Direct in-image targets: 0x4d5a9, 0x4d60e

### RVA `0x4e308`–`0x4e40f` (0x107)
- Decode ratio: `1.0`; instructions: `75`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!WriteFile×1
- Direct in-image targets: 0x3cfb0, 0x3dc30, 0x4e3e4

### RVA `0x4d430`–`0x4d52d` (0xfd)
- Decode ratio: `1.0`; instructions: `68`
- Imports: kernel32.dll!GetFileType×1, kernel32.dll!GetStartupInfoW×1
- Direct in-image targets: 0x52b38, 0x57920

### RVA `0x3f4e8`–`0x3f5a7` (0xbf)
- Decode ratio: `1.0`; instructions: `53`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×1
- Direct in-image targets: 0x3f584, 0x3f58c, 0x3f597, 0x42a4c, 0x42a94, 0x42ff0, 0x49540

### RVA `0x52784`–`0x52820` (0x9c)
- Decode ratio: `1.0`; instructions: `46`
- Imports: kernel32.dll!FreeEnvironmentStringsW×1, kernel32.dll!GetEnvironmentStringsW×1
- Direct in-image targets: 0x4bc20, 0x4bc80, 0x57270

### RVA `0x4dd54`–`0x4dddf` (0x8b)
- Decode ratio: `1.0`; instructions: `40`
- Imports: kernel32.dll!FlushFileBuffers×1, kernel32.dll!GetLastError×1
- Direct in-image targets: 0x494dc, 0x49500, 0x52be0, 0x52cc8, 0x52eec

### RVA `0x4dc00`–`0x4dc88` (0x88)
- Decode ratio: `1.0`; instructions: `44`
- Imports: kernel32.dll!GetFileSizeEx×1, kernel32.dll!SetFilePointerEx×1
- Direct in-image targets: 0x4dc82, 0x52eec

### RVA `0x43060`–`0x430ca` (0x6a)
- Decode ratio: `1.0`; instructions: `30`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×1
- Direct in-image targets: 0x4309a, 0x4ba7c

### RVA `0x430cc`–`0x43118` (0x4c)
- Decode ratio: `1.0`; instructions: `22`
- Imports: kernel32.dll!GetLastError×1, kernel32.dll!SetLastError×1
- Direct in-image targets: 0x43104

### RVA `0x23050`–`0x2379a` (0x74a)
- Decode ratio: `1.0`; instructions: `463`
- Imports: kernel32.dll!CloseHandle×2
- Direct in-image targets: 0x2560, 0x2570, 0x22e40, 0x22f90, 0x23750, 0x23752, 0x23bc0, 0x23d00, 0x23dc0, 0x248e0, 0x27020, 0x3cfb0, 0x3d36c, 0x43404, 0x57170, 0x57270

### RVA `0x181a0`–`0x186f6` (0x556)
- Decode ratio: `1.0`; instructions: `367`
- Imports: kernel32.dll!CloseHandle×2
- Direct in-image targets: 0x1828f, 0x18380, 0x1844c, 0x184b9, 0x18570, 0x186a3, 0x3cfb0, 0x42d5c, 0x57920

### RVA `0x5275c`–`0x52781` (0x25)
- Decode ratio: `1.0`; instructions: `8`
- Imports: kernel32.dll!GetCommandLineA×1, kernel32.dll!GetCommandLineW×1
- Direct in-image targets: (none)

### RVA `0x49558`–`0x495ae` (0x56)
- Decode ratio: `1.0`; instructions: `25`
- Imports: kernel32.dll!IsProcessorFeaturePresent×1
- Direct in-image targets: 0x43118, 0x4a4e0, 0x507c4, 0x50814
