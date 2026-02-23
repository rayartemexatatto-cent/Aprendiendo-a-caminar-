
## 2025-01-23 - Accessibility in CSS Utilities
**Learning:** Utility classes for animations often lack accessibility considerations like `prefers-reduced-motion`. In a design system, these utilities should default to respecting user preferences to prevent motion sickness and improve accessibility without requiring every consumer to implement the media query themselves.
**Action:** When adding or modifying animation utilities, always include a `@media (prefers-reduced-motion: reduce)` block that either stops the animation, speeds it up to be instant, or reduces it to a safe level (like slowing down a spinner).
