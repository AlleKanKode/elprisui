# Nordic Kinetic Design System

### 1. Overview & Creative North Star
**Creative North Star: The Energetic Minimalist**
Nordic Kinetic is a high-performance design system that fuses Scandinavian restraint with high-octane energy. It moves away from static, boxy layouts toward a fluid, editorial feel. The system prioritizes breathing room (whitespace) and uses "The Glow"—a signature radial aura—to signify active states and positive environmental impact. By combining heavyweight typography with thin, architectural lines and vibrant neon accents, the system feels both grounded and futuristic.

### 2. Colors
The palette is built on a foundation of "Nordic Grays" and "Deep Forest" blacks, punctuated by a high-visibility "Electric Lime" primary.

*   **Primary (#0df259):** Reserved for high-priority actions, success states, and live energy tracking.
*   **Surface Hierarchy:**
    *   **Background (#FFFFFF):** The canvas for all content.
    *   **Surface Container Low (#F8FAF9):** Used for large structural sidebars to provide a soft distinction from the main content.
    *   **Surface Container High (#E1E8E3):** Used for subtle dividers and thin borders.
*   **The "No-Line" Rule:** Sectioning should be achieved through background shifts (e.g., transitioning from white to `#F8FAF9`). 1px borders are permitted only when using `Nordic-Gray` to define specific utility cards.
*   **The "Glass & Gradient" Rule:** Use `rgba(13, 242, 89, 0.15)` as a radial background ("Status Glow") for hero sections to create a sense of atmospheric depth without heavy shadows.

### 3. Typography
The system uses **Manrope** exclusively to maintain a modern, technical yet approachable voice. It utilizes a dramatic scale to create an editorial hierarchy.

*   **Display (4.5rem / 72px):** Used for critical data points like energy prices. Font weight: Black (900).
*   **Headline 1 (2.25rem / 36px):** High-impact section starts. Font weight: Extrabold.
*   **Headline 2 (1.5rem / 24px):** Standard section headings. Font weight: Bold.
*   **Body (1rem / 16px):** Primary reading text. Font weight: Medium (500).
*   **Label/Caption (0.75rem / 12px):** Uppercase with wide tracking (0.1em) for status indicators and micro-copy.

The contrast between the 4.5rem data and 0.75rem labels creates the "Kinetic" energy of the brand.

### 4. Elevation & Depth
Nordic Kinetic rejects traditional heavy shadows in favor of **Tonal Layering** and **Ambient Glows**.

*   **The Layering Principle:** Depth is created by nesting white cards inside `#F8FAF9` containers. 
*   **Ambient Shadows:** For hover states, use a "Primary Glow" shadow: `0 20px 25px -5px rgba(13, 242, 89, 0.05)`.
*   **Shadow-SM:** Use a standard `0 1px 2px 0 rgba(0, 0, 0, 0.05)` for small interactive elements like icon containers.
*   **Status Glow:** A radial gradient `radial-gradient(circle, rgba(13, 242, 89, 0.15) 0%, rgba(255, 255, 255, 0) 70%)` is used to elevate hero content.

### 5. Components
*   **Primary Action Button:** Black background (`#0D1C12`), white text, `1rem` (xl) rounded corners. On hover, apply a `scale-105` transition.
*   **Ghost Buttons:** Transparent background with `Nordic-Gray` borders and `Deep Forest` text.
*   **Impact Cards:** White background, 1px `Nordic-Gray` border. Icon containers inside cards use `#F5F8F6` to create nested depth.
*   **Status Badges:** Pill-shaped, using `primary/20` background with `primary-dark` text. Must include a pulsing `2x2` dot for "live" states.
*   **Progress Bars:** Thin `8px` tracks in `Nordic-Gray` with `Primary` fills to denote achievement.

### 6. Do's and Don'ts
*   **Do:** Use extreme typographic scale to highlight the most important data point on the screen.
*   **Do:** Use 16px (lg) and 20px (xl) corner radii for a friendly, modern feel.
*   **Don't:** Use standard blue for links; use `Primary-Dark` (#0A8A35) or Black.
*   **Don't:** Use heavy drop shadows. If an element needs to pop, use a background color shift or a very subtle primary-tinted glow.
*   **Do:** Maintain a "Sticky Sidebar" for navigation to anchor the layout while the main content remains fluid and editorial.