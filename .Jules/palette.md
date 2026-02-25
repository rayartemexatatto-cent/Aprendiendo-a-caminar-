# Palette's Journal

## 2025-02-17 - Ensuring Final State Visibility for Reduced Motion

**Learning:** When disabling animations for `prefers-reduced-motion: reduce`, simply setting `animation: none` is insufficient if the element's base style hides it (e.g., `opacity: 0`, `width: 0`). Animation utilities often rely on `animation-fill-mode: forwards` to keep the element visible. Without the animation, the element remains in its initial hidden state.

**Action:** Always explicitly force the "final visible state" (e.g., `opacity: 1 !important`, `width: 100% !important`, `transform: none !important`) within the reduced motion media query to ensure content is accessible.
