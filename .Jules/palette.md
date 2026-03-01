# YYYY-MM-DD - Initial Journal Entry

## 2024-03-01 - Respecting prefers-reduced-motion for animations
**Learning:** Found that animation utility classes might run default animations regardless of user preference, potentially causing issues for users with vestibular disorders. Setting duration and delay to 0s with `!important` inside an `@media (prefers-reduced-motion: reduce)` block effectively stops both CSS animations and transitions gracefully without breaking components that rely on transitionend/animationend events (since they fire immediately).
**Action:** Created a global reduced motion media query block in `src/utilities/animations.scss` to target all custom animation/transition utility classes (e.g., `.anim-fade-in`, `.anim-rotate`, `.hover-grow`) and force durations/delays to 0s.
