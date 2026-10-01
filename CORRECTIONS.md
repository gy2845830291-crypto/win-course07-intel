# 情报包修正说明（本机实测核验，2026-10-01）

对 `XWGZ_NoCardKey_进展_20260909.zip` 的核验结果。
核验对象：`D:\XWGZ_rt66\rt_full\UeVerify.dll`（5,182,464 bytes，SHA256 `193889bd6fa55d5b78489ab3a5f37a82...`）

## 结论一：PATCH_NOTES 的 OFFSET 列可靠，函数名标签错误

原 `PATCH_NOTES.txt` 六行中，OFFSET↔RVA 的换算**全部自洽**（已逐一验证），
但**函数名与 RVA 的绑定有四处张冠李戴**。

### 真实导出表（从导出表直接读取，权威）

| 函数 | 真实 RVA | PATCH_NOTES 写的 RVA | 判定 |
|---|---|---|---|
| `UeSetVerify` | `0xD400` | `0xd400` | 正确 |
| `UeGetBinduuid` | `0xD410` | `0xd5d0` | **错** |
| `UeGetVersion` | `0xD4E0` | `0xd410` | **错** |
| `UeLogin` | `0xD5D0` | `0xd4e0` | **错** |
| `UeSetBinduuid` | `0xD840` | `0xd6a0` | **错** |
| `UeModuleMd5` | `0xD6A0` | `0xd840` | **错** |

### 经核验的 OFFSET 表（可直接使用）

| 函数 | 文件偏移 | PATCH_BYTE | 字节数 |
|---|---|---|---|
| `UeSetVerify` | `0xc800` | `b801000000c3` | 6 |
| `UeGetBinduuid` | `0xc810` | `b801000000c3` | 6 |
| `UeGetVersion` | `0xc8e0` | `b801000000c3` | 6 |
| `UeLogin` | `0xc9d0` | `b801000000c3` | 6 |
| `UeSetBinduuid` | `0xcaa0` | `b801000000c3` | 6 |
| `UeModuleMd5` | `0xcc40` | `b801000000c3` | 6 |

（`mov eax,1; ret`，恒返回 1）

### 为什么功能上仍然可用

六个函数被 patch 成**完全相同**的字节序列，所以"哪个偏移贴哪个名字"
不影响最终行为——六个导出一律返回 1。
但**语义推理会错**：若按原名字去理解"UeLogin 在 0xc8e0"，
得到的调用链分析是错的。递给下游分析者前必须纠正。

## 结论二：本机 rt66 的 UeVerify.dll 已被 patch 过

核验时六个偏移处的实际字节**已经是** `b801000000c3`：

```
UeSetVerify     0xc800: b801000000c3 0fb6c1c3cccccccccccc
UeGetVersion    0xc810: b801000000c3 56574883ec30488b059d
UeLogin         0xc8e0: b801000000c3 5641574883ec48488b05
UeSetBinduuid   0xcaa0: b801000000c3 5657415641574883ec50
UeModuleMd5     0xcc40: b801000000c3 89742420574881ec7001
```

即这台机器上的 `D:\XWGZ_rt66\rt_full\UeVerify.dll` 是**已打补丁状态**，
不是原始 DLL。若需要原始字节做对照，应从情报包
`00_最终交付_123_NoCardKey_Release\UeVerify.dll` 之外的未修改副本取。

注意：情报包内那份 `UeVerify.dll`（SHA256 `6631bc22...`）也是 patched 版，
与 `dryrun_out`、`intel_dll` 三份哈希一致，都是打过补丁的。

## 结论三：情报包样本与 6.9 不是同一文件

| 样本 | 大小 | SHA256（前 32） |
|---|---|---|
| 换肤程序 6.9（手上） | 26,426,880 | `eef7de5767b0e625aea4e6b3cd2f8b14515...` |
| 换肤程序 6.6（手上） | 26,072,064 | `573693e5c57695da41ea424058788095a0fb...` |
| 情报包 `123.exe` | 25,916,416 | `f192434bdc4448534f409c490e0fef48aa0...` |

三者互不相同。但 `123.exe` 与 6.9 的**节区结构同构**
（均为 8 节，含 `.ace0` / `.fptable` / `.rsrc`，同 x64 PE32+），
说明同一 ACE 壳打包器、同一产品家族的不同版本。

**因此情报可迁移，但偏移需重新核验**——不能直接假设 6.9 的
UeVerify.dll 内部偏移与 123.exe 版本一致。

## 结论四：动态方案的协议常量（已验证可复用）

`bypass_launcher.py` 中的常量来自服务端源码还原，与样本版本无关：

- `PROTOCOL_TOKEN = 8RkF8FP6e2R8rJwGrmA38NKbfp8QaA22`
- `ENCRYPT_KEY = 75e0308b4dfce9fd8f4940408de683b7c6c9f3da116570456f83e5ec0718be6e`
- 协议：RC4（key = md5(user + TOKEN + udid) 小写）+ 双层 MD5 签名
- 外签：`md5(str(ts)[:8] + user + udid)` 小写
- 内签：`md5(user + vipExpDate + vipExpTime + ts + udid)` 大写
- VIP 到期：`4102444799`（2099-12-31 23:59:59）
- 拦截点：`WinHttpReadData` 回注响应体

这套是**协议层**的，不依赖二进制偏移，6.9 若走同一鉴权服务则直接可用。

## 使用建议

按可靠性排序：

1. **动态方案**（协议伪造）—— 与样本版本无关，优先用
2. **静态 stub** 的 `PATCH_BYTE` 与偏移量 —— 可用，但标签需按上表纠正
3. **函数名语义** —— 别信原 PATCH_NOTES 的绑定
