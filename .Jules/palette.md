## PALETTE'S JOURNAL

## 2024-05-22 - [Initial Setup]
**Learning:** This repo is `primer/css`, a pure CSS/SCSS design system. It doesn't have React components or HTML templates to modify directly.
**Action:** Focus on CSS utility classes that enable better UX/a11y when used by consumers. Look for missing utility classes for things like reduced motion, focus visibility, or screen reader only text.

## 2024-05-22 - [Animations and Accessibility]
**Learning:** The `src/utilities/animations.scss` file contains several animations but lacks `prefers-reduced-motion` queries. This means users who have requested reduced motion in their OS settings will still see these animations, which can trigger vestibular disorders.
**Action:** Wrap animations in `@media (prefers-reduced-motion: no-preference)` or provide a utility class to disable animations based on preference.
