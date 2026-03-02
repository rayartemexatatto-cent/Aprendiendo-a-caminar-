# Palette Journal

## 2025-03-02 - Ensure animations respect user preference for reduced motion
**Learning:** Utilities that provide animation options must inherently include safeguards for accessibility out-of-the-box. We noticed that animation utilities, such as `.anim-fade-in` and others located in `src/utilities/animations.scss`, lacked `prefers-reduced-motion` declarations.
**Action:** Always wrap animations in `prefers-reduced-motion: reduce` with `0s` duration to comply with accessibility standards across our design system automatically. This eliminates the burden of manual oversight.
