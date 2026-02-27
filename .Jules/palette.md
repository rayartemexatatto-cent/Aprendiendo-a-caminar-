# Palette's UX Learnings\n

## 2025-02-17 - Respecting Reduced Motion Preferences in Global Utilities
**Learning:** In a large design system like Primer, adding a single media query (`@media (prefers-reduced-motion: reduce)`) at the root of reusable animation classes (e.g., `.anim-*`) provides a massive accessibility win for users prone to motion sickness or vestibular disorders, without having to patch individual components.
**Action:** When creating or maintaining animation utility classes, always ensure they are wrapped or overridden by `prefers-reduced-motion` media queries that set `animation-duration: 0s` and `transition-duration: 0s`.
