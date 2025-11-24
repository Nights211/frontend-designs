# Minimalist Centered

A radical minimalist landing page with editorial-style layouts, scroll-snapping sections, and asymmetric design.

## Design Philosophy

This template takes a completely different approach to minimalism:
- **Editorial/Magazine Style** - Inspired by high-end print design
- **Asymmetric Layouts** - Nothing is centered, everything is intentionally offset
- **Scroll Snapping** - Each section takes full viewport height
- **Monochrome Base** - Pure black and white with single accent color
- **Typography as Design** - Huge letters and numbers as visual elements
- **Negative Space** - Intentional emptiness as a design feature

## Unique Features

### Layout Innovations

1. **Vertical Typography** - Large "MINIMAL" text written vertically as design element
2. **Scroll Snap Sections** - Full-screen sections that snap on scroll
3. **Dot Navigation** - Side navigation showing scroll progress
4. **Huge Numbers** - Oversized numbers (01, 02) as visual anchors
5. **Asymmetric Hero** - Content offset to one side, not centered
6. **Single Column Features** - List-style features with numbers, not cards
7. **Inverted Quote Section** - Black background with white text
8. **Bottom-Aligned Contact** - Form positioned at bottom of viewport

### Design Elements

- **No Cards** - Everything is text, lines, and whitespace
- **No Grids** - Single column, stacked layouts
- **Minimal Color** - Black, white, and one accent (red/pink)
- **Editorial Typography** - Large, light font weights
- **Line Separators** - Simple horizontal lines as dividers
- **Hover Transitions** - Subtle color and position changes

## Sections

1. **Hero** - Vertical text + offset content with CTA
2. **Number Section** - Giant "01" with stats inline
3. **Features** - Numbered list (01-04) with descriptions
4. **Quote** - Full-screen inverted section with testimonial
5. **Contact** - Bottom-aligned form with links

## Tech Stack

- HTML5
- CSS3 (Scroll Snap, Flexbox, Custom Properties)
- Vanilla JavaScript (Intersection Observer, Scroll Events)

## Color Scheme

- Background: `#ffffff` (white)
- Text: `#000000` (black)
- Accent: `#ff3366` (red/pink)
- Gray: `#666666` (muted text)
- Light Gray: `#f5f5f5` (subtle backgrounds)

## Typography

- System fonts for clean look
- Light weights (300-400) for elegance
- Huge sizes for impact (up to 20rem)
- Vertical text for visual interest

## Key Differences from Other Templates

Unlike full-width-hero and other templates, this design:
- Uses scroll snapping (full-screen sections)
- Has asymmetric, editorial layouts
- Features vertical typography
- Uses huge numbers as design elements
- Has inverted color section (black background)
- No cards or grids - just text and lines
- Side dot navigation instead of top nav
- Bottom-aligned contact form
- Monochrome with single accent color

## Usage

Open `index.html` in a browser or use the launcher:

```bash
./launch.py landing minimalist-centered
```

## Customization

Edit CSS variables in `style.css`:

```css
:root {
    --accent: #ff3366;    /* Accent color */
    --bg: #ffffff;        /* Background */
    --text: #000000;      /* Text color */
    --gray: #666666;      /* Muted text */
}
```

## Scroll Behavior

- Sections snap to viewport on scroll
- Smooth scrolling enabled
- Dot navigation tracks current section
- Click dots to jump to sections

## Responsive Design

- Vertical text hidden on mobile
- Stats stack vertically on small screens
- Features become single column
- Dot navigation hidden on mobile
- All text sizes scale with viewport

## Browser Support

- Modern browsers with scroll-snap support
- CSS Custom Properties
- Intersection Observer API
- Flexbox
