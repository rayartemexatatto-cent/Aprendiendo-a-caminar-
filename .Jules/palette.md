## 2026-02-21 - Explicit Cursor for Disabled States
**Learning:** Browser defaults for disabled inputs are inconsistent (often just the default pointer or I-beam). Adding `cursor: not-allowed` provides immediate, clear feedback that the element is non-interactive, improving accessibility for all users, especially those with cognitive disabilities who rely on visual cues.
**Action:** Always verify disabled states include `cursor: not-allowed` or `cursor: default` (if system standard) rather than relying on browser defaults.
