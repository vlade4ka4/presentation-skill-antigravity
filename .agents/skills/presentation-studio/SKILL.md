---
name: presentation-studio
description: Generates high-impact presentation slide decks with Swiss/Bento design, single-file HTML runtime, speaker notes, keyboard navigation, and export to PDF/PPTX.
---

# Presentation Studio & Slide Deck Engine (Antigravity Skill)

This skill enables Antigravity to craft world-class presentation slide decks inspired by Apple Keynote, Linear, and Swiss editorial design, with zero bloated external dependencies and full offline browser support.

---

## 1. Output Modes

| Mode | Format | When to Use | Output |
| :--- | :--- | :--- | :--- |
| **Native PowerPoint** (Primary) | **`.pptx`** | **Strict requirement for clients/colleagues** to open, edit, and present in Microsoft PowerPoint. | Fully editable native `.pptx` with 100% vector shapes, editable text blocks, 16:9 widescreen, Bento-style cards. |
| **Interactive Web Deck** | **`.html`** | Fast in-browser review, web presentation, or instant 1-click PDF export via `Ctrl+P`. | Standalone `.html` with keyboard navigation, full-screen mode, and responsive layout. |

---

## 2. Design Standards & Visual Hierarchy

Every generated slide deck MUST clear these design principles:

1. **Aspect Ratio**: Always locked to standard **16:9** (1920×1080 canvas or fluid aspect ratio `aspect-ratio: 16 / 9`).
2. **Typography**:
   - Headings: Bold grotesque / system geometric fonts (`system-ui`, `-apple-system`, `Inter`, `Segoe UI`).
   - Tracking: `-0.02em` for large titles (>=32px).
   - Unitless line-height: `1.1–1.2` for titles, `1.4–1.5` for descriptions.
   - Numbers: `font-variant-numeric: tabular-nums` for metrics, stats, and prices.
3. **Layout Discipline**:
   - Never place more than **1 core idea** per slide.
   - Use **Bento Grid** (2-4 cards with subtle `1px` border, soft shadows, rounded corners `16px–24px`).
   - Visual anchors: Large metric/stat numbers (e.g., `+140%`, `3.5x`, `99.9%`) paired with short descriptive labels.
4. **Color Systems**:
   - **Dark Keynote Theme** (Default): Background `#0b0f19`, Surface Card `#161f30` or `rgba(255,255,255,0.04)`, Border `rgba(255,255,255,0.08)`, Accent `#3b82f6` or `#10b981`.
   - **Swiss Light Theme**: Background `#f8fafc`, Surface Card `#ffffff`, Border `#e2e8f0`, High-contrast text `#0f172a`, Sharp Accent `#e11d48` or `#2563eb`.

---

## 3. Interactive Web Deck Engine Features

Every generated HTML slide deck contains an embedded lightweight JS controller:

- ⌨️ **Keyboard Controls**:
  - `→` / `Space` / `PageDown`: Next slide
  - `←` / `PageUp`: Previous slide
  - `Home` / `End`: First / Last slide
  - `F`: Toggle Fullscreen
  - `O`: Toggle Overview Grid (thumbnail view of all slides)
  - `S`: Toggle Speaker Notes window (shows current slide, next slide preview, timer, notes)
- 🖨️ **Print-to-PDF Ready**:
  ```css
  @media print {
    @page { size: 16in 9in landscape; margin: 0; }
    body { background: transparent; }
    .slide { page-break-after: always; break-after: page; width: 100vw; height: 100vh; display: flex !important; }
    .controls, .speaker-notes, .progress-bar { display: none !important; }
  }
  ```

---

## 4. Standard Slide Types & Templates

1. **Title / Cover Slide**: Large impactful headline, subtitle, author/team badge, date.
2. **Problem vs. Solution**: 2-column comparison with distinct visual badges (Red/Gray for Problem, Green/Blue for Solution).
3. **Bento Feature Grid**: 3 or 4 cards with asymmetric sizes displaying key features, icons, or stats.
4. **Key Metrics / Big Numbers**: 3 large data points with percent growth and explanation.
5. **Timeline / Roadmap**: Sequential milestones with status badges (Completed, In Progress, Planned).
6. **Closing / Call to Action**: Final takeaway, contact info, next steps.

---

## 5. Workflow for the Agent

When the user requests a presentation:
1. **Analyze Subject & Structure**: Clarify target audience and slide count (typically 4–8 slides for a punchy deck).
2. **Choose Theme**:
   - **Modern Dark (Default)**: Deep Navy `#0b0f19`, Card Surface `#161f30`, Accent `#38bdf8`, Text `#f8fafc`.
   - **Corporate Light**: Crisp White `#ffffff`, Card Surface `#f8fafc`, Border `#e2e8f0`, Accent `#2563eb`, Text `#0f172a`.
3. **Generate Native `.pptx`**:
   - Execute a Python script using `python-pptx` (which is installed and verified on this machine).
   - Set 16:9 widescreen (`prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)`).
   - Create fully editable shapes (`ROUNDED_RECTANGLE`), formatted text frames with `word_wrap = True`, Segoe UI font, and proper vertical margins.
   - Save the `.pptx` directly into the workspace and provide a clickable file link.
4. **Deliver to User**: Output the link to the `.pptx` file so the user can open and edit it in PowerPoint immediately.
