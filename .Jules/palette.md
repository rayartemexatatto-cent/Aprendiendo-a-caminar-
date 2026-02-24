# Palette's UX Journal

## 2026-02-24 - Tooltips and Reduced Motion
**Learning:** The `@primer/css` tooltips rely on CSS animations (`tooltip-appear`) for interaction feedback. These animations lacked support for `prefers-reduced-motion: reduce`, potentially causing discomfort for users with vestibular disorders.
**Action:** When implementing or auditing CSS-based components, always verify `prefers-reduced-motion` support. For `@primer/css`, ensure any new animation includes a media query override setting `animation: none` or reducing duration to 0s.
