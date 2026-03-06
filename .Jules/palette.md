## 2024-05-28 - Missing Reduced Motion Support in Utility Animations
**Learning:** Found that core utility animations (`.anim-fade-in`, `.anim-rotate`, etc) did not respect the user's OS-level reduced motion preferences. When building a UI library used by millions, utility classes must default to accessible behavior so that consumers of the library automatically inherit good a11y practices.
**Action:** Always wrap animation and transition utility classes with `@media (prefers-reduced-motion: reduce)` to set durations and delays to `0s !important`.
