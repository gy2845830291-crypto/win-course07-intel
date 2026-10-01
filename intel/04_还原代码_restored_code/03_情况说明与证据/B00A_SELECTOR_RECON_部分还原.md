# B00A Natural Selector Reconstruction (dens90-era)

## Status
PARTIAL — fail-chain mapped; true license boolean still OPEN. Harness pass uses FORCE MBA + one-shot ring divert.

## Fail-chain (CLOSED map)
```
0x4b743a jo
0x49cf87 call
0x2a4859 call
0x2d5766 jne
~0x2a3de8
0x2b108c call          ; FAIL ENTRY
0x49bfa5 jmp 0x24b650
0x20b091 call 0x3348a6
0x3348a6: eax=[rbx-6]; xor/neg/inc opaque
0x43902b jge 0x321418  ; ALWAYS taken once entered (SF=OF=0)
0x321418 / 0x321463 call 0x4542ac  ; FAILENC pusher
0x4542bc call 0x43ecb5             ; pushes FAIL_ENC
```
Opposite edge `0x439031` never seen with current SERIAL/LICENSE_BLOB candidate.

## MBA status materialize (CLOSED dens39/83/85)
- VIP_FAIL `0x54D85BC4` → xor/`0xFFDE6403` → rol1 → lea/r11=`0xFFFFFFAF`/−`0x4A5C7E7E` → bswap → `0xC000B00B` → dec → **`0xC000B00A`**
- VIP_PASS `0x5A705B64` → same → **status 0** (`passOk`)

## Secondary windows
- `0x43B24A` cmp r8,r9 / `0x43B24D` ja
- dens19 invert site `jbe @ 0x20B917`
- Ring observe only: `0x400f92` / do **not** Interceptor-attach `0x400fc3`/`0x400fc7`

## CHECK_FN (local fixture model)
1. Build/verify response → VIP imm stream at `UMOD+0x1fac60`
2. Upstream dispatcher chooses enter-fail (`0x2b108c`) vs pass fallthrough (missing natural witness)
3. If fail-chain entered → opaque jge → FAILENC → MBA → `0xC000B00A`
4. If VIP_PASS planted + ring completes → status 0

## OPEN
Who writes the boolean that avoids `0x2b108c` under real SERIAL/LICENSE_BLOB.
Post-pass `.uyB` mutation / Ace (separate; dens87–90 forced/cave paths did not mutate `.uyB`).
