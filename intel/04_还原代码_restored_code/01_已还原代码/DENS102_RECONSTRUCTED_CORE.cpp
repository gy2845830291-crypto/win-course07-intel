// Source-level reconstruction from SAMPLE_dens102_hist_h4000_text_denser_asInvoker.exe.
// Function RVAs and control-flow/error semantics are retained in comments.

#include <windows.h>
#include <cstdint>
#include <cstddef>

namespace dens102 {

static uint32_t fnv1a(const char* s) {
    uint32_t h = 0x811C9DC5u;
    while (*s) {
        h = (h ^ static_cast<uint8_t>(*s++)) * 0x01000193u;
    }
    return h;
}

// RVA 0x21ef0-0x220f1.
// The fallback PEB/export walk searches for FNV-1a 0x54A79208, which resolves
// to ntdll!RtlNtStatusToDosError on the analysis host.
static DWORD resolve_import(
    const char* module_name,
    const char* proc_name,
    FARPROC* result
) {
    HMODULE module = GetModuleHandleA(module_name);
    if (!module) module = LoadLibraryA(module_name);

    if (module) {
        FARPROC proc = GetProcAddress(module, proc_name);
        if (proc) {
            if (result) *result = proc;
            return ERROR_SUCCESS;
        }
    }

    // Original code performs a manual PEB loader-list/export-directory walk.
    // Equivalent source-level behavior:
    using RtlNtStatusToDosError_t = ULONG (WINAPI*)(LONG);
    auto ntdll = GetModuleHandleW(L"ntdll.dll");
    auto convert = reinterpret_cast<RtlNtStatusToDosError_t>(
        GetProcAddress(ntdll, "RtlNtStatusToDosError")
    );
    return convert ? convert(static_cast<LONG>(0xC0000135u))
                   : ERROR_MOD_NOT_FOUND;
}

struct FileVtable;
struct FileContext {
    FileVtable* vtable; // +0x00
    HANDLE handle;      // +0x08
    uint8_t path_state[0x20];
    bool open_flag;     // +0x2c
};

// The calls through vtable offsets +0x58/+0x40 are preserved as preflight
// checks in the binary.  Their concrete class names are not present.
static bool preflight(FileContext* self);
static bool prepare_io(FileContext* self, uint64_t position, uint32_t flags);

// RVA 0x22b00-0x22b5a.
static bool seek(FileContext* self, LARGE_INTEGER distance, DWORD method) {
    if (!preflight(self)) return false;
    return SetFilePointerEx(self->handle, distance, nullptr, method) != FALSE;
}

// RVA 0x22b60-0x22bea.
static bool read_exact(
    FileContext* self,
    void* buffer,
    uint32_t size,
    uint64_t position
) {
    if (!preflight(self) || !prepare_io(self, position, 0)) return false;
    DWORD transferred = 0;
    return ReadFile(self->handle, buffer, size, &transferred, nullptr) != FALSE
        && transferred == size;
}

// RVA 0x22bf0-0x22c7f.
static bool write_exact(
    FileContext* self,
    const void* buffer,
    uint32_t size,
    uint64_t position_or_zero
) {
    if (!preflight(self)) return false;
    if (position_or_zero && !prepare_io(self, position_or_zero, 0)) return false;
    DWORD transferred = 0;
    return WriteFile(self->handle, buffer, size, &transferred, nullptr) != FALSE
        && transferred == size;
}

// RVA 0x22cb0-0x22d1f.  The original stores only the low 32 bits.
static bool size32(FileContext* self, uint32_t* result) {
    if (!result || !preflight(self)) return false;
    LARGE_INTEGER size{};
    if (!GetFileSizeEx(self->handle, &size)) return false;
    *result = size.LowPart;
    return true;
}

// RVA 0x22d20-0x22d57.
static bool close(FileContext* self) {
    if (!self->handle) return false;
    const bool ok = CloseHandle(self->handle) != FALSE;
    self->handle = nullptr;
    self->open_flag = false;
    return ok;
}

// RVAs 0x2bf10-0x2c17c reconstruct a reverse bitstream used by the
// entropy/sequence decoder.  Layout matches the observed fields.
struct ReverseBitStream {
    uint64_t bit_container; // +0x00
    uint32_t bits_consumed; // +0x08
    uint8_t* limit_ptr;     // +0x10
    uint8_t* start;         // +0x18
    uint8_t* ptr;           // +0x20
};

// RVA 0x2c0c0.
static uint64_t peek_bits(const ReverseBitStream& bs, uint32_t count) {
    const uint32_t shift = 64u - (bs.bits_consumed + count);
    const uint64_t mask = count == 64 ? ~0ull : ((1ull << count) - 1ull);
    return (bs.bit_container >> shift) & mask;
}

// RVA 0x2c0e0.
static uint64_t read_bits(ReverseBitStream& bs, uint32_t count) {
    const uint64_t value = peek_bits(bs, count);
    bs.bits_consumed += count;
    return value;
}

// RVA 0x2d470: one entropy-state transition.  Each 8-byte table entry contains
// new-state base at +4 and number-of-bits at +2.  This is the table shape used
// by FSE/tANS sequence decoding.
struct FseEntry {
    uint16_t symbol;
    uint8_t number_of_bits;
    uint8_t reserved;
    uint32_t new_state_base;
};

static uint32_t decode_fse_state(
    ReverseBitStream& bits,
    const FseEntry* entry,
    uint32_t* state
) {
    const uint32_t extra = static_cast<uint32_t>(read_bits(bits, entry->number_of_bits));
    *state = entry->new_state_base + extra;
    return entry->symbol;
}

// RVA 0x2d4c0-0x2dbd8 is the recovered sequence-decompression core.  It keeps
// three FSE states, decodes literal length / match length / offset, maintains
// three repeat offsets at object +0x683c, and emits matches in 16/32-byte copy
// loops.  Those traits identify a Zstandard-style sequence decoder rather than
// generic file encryption.  Full register-accurate control flow is preserved
// in DENS102_FUNCTION_MAP.json and the PE itself.

} // namespace dens102
