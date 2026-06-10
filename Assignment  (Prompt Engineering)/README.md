
# DevOS — AI Developer Growth OS

**An AI-powered career operating system for software engineers.**  
Analyze skills, close gaps, generate personalized roadmaps, simulate interviews, and track your path from mid-level to Staff Engineer — all inside a single, beautifully engineered interface.


## The Problem

Most developers plateau not from lack of effort, but from lack of visibility.

They don't know which skills are holding them back from their next promotion. They don't know how their GitHub profile reads to a recruiter. Their resume gets filtered out by ATS before a human ever sees it. They practice LeetCode without context, interview without structure, and chase career goals without a real map.

Existing tools address these in isolation — a resume checker here, a LeetCode tracker there. None of them connect the full picture.

---

## The Solution

DevOS treats your career as a system that can be observed, analyzed, and optimized.

It combines seven analytical modules — skill gap analysis, resume intelligence, GitHub insights, AI roadmap generation, interview simulation, and career trajectory forecasting — into a single interface that gives you the complete picture of where you are and a concrete plan to get where you're going.

The interaction model is deliberate: every screen surfaces one primary insight and one recommended action. There's no noise, no feature overload, just the information that moves the needle.

---

## Features

### Career Command Dashboard
The entry point into your career data. Displays four composite scores — Career Health, AI Growth Score, Job Readiness, and Skill Momentum — as animated SVG rings with real-time glow effects. Includes a live six-axis radar chart across Frontend, Backend, Cloud, Security, AI/ML, and DevOps dimensions, a 26-week contribution heatmap with four intensity levels, daily activity bar charts, and a skill progress breakdown with color-coded proficiency tiers.

### Career Growth Universe (Live Canvas Visualization)
The signature feature of the Dashboard. Built entirely on the HTML5 Canvas 2D API with a custom animation loop running at 60fps. Renders skill nodes as radial-gradient spheres that float with independent velocity vectors and bounce off canvas boundaries. Distance-based connection lines are drawn between nearby nodes with opacity proportional to proximity. Node radius scales linearly with mastery level; color encodes proficiency tier across five bands. No third-party charting library involved — the entire physics simulation is hand-written.

### AI Skill Constellation Map
A polar-coordinate SVG visualization that places skills as nodes on an abstract star map. Node size is proportional to mastery. SVG polylines with `stroke-dasharray` connect related skill clusters. Includes a legend for four proficiency tiers (Expert/Proficient/Developing/Beginner) and surfaces an AI-generated gap analysis identifying the three highest-leverage skills missing from a target role's requirements.

### Resume Intelligence Engine
Multi-dimensional resume scoring across five sections: Summary, Experience, Skills, Education, and Projects. Produces an overall score, an ATS compatibility score, and a keyword-match score displayed as independent rings. Each improvement suggestion is categorized by type (ATS, Impact, Skills, Brand, Links) and priority level (Critical/High/Medium/Low). Includes a projected score uplift with estimated callback rate improvement — the kind of output that makes the ROI of the tool immediately clear.

### GitHub Repository Insights
Parses repository metadata to surface language distribution as a proportional bar chart, contribution quality metrics (code quality, documentation depth, test coverage, commit consistency), and star rankings. Includes repository cards with language color indicators matching GitHub's official palette. Highlights the highest-leverage action — for example, flagging a high-star repo with zero test files.

### AI Growth Roadmap
A vertical milestone timeline with three states: completed (emerald), active (pulsing blue), and upcoming (muted). Clicking any node loads its detail panel on the right — title, description, progress bar, estimated weeks remaining, and AI coach insights. The companion panel also renders a six-month trajectory estimate to Staff Engineer based on current pace. Built with no timeline library; the connector lines and state machine are pure CSS and React state.

### AI Interview Simulator
A two-stage flow: category selection with an animated AI orb, then an active session view. Categories include Algorithms, System Design, React/Frontend, Behavioral, and Database. Each session surfaces a question with difficulty and category tags. Answers are submitted to a scoring view that returns a numeric score via an animated ring, followed by structured feedback broken into strengths, gaps, and specific technical recommendations. The AI orb uses a `box-shadow` pulse animation that communicates "live session" without being distracting.

### Career Command Center
Surfaces an opportunity radar with company-match percentages for real companies (Vercel, Stripe, Linear, Notion). Includes a Future Career Simulator that projects role title and compensation at 3, 6, and 12 months based on the current skill growth rate. The weekly priority board shows the three highest-leverage tasks for the current week, with urgent items marked and completed items rendered with strikethrough.

### Landing Page
A full marketing page with a cinematic hero section: aurora background (two CSS pseudo-element radial gradients animating on independent keyframe paths), a 60×60px CSS grid overlay, three floating preview cards that idle on independent float animation timings, and animated stat counters that fire on scroll via `IntersectionObserver` using a cubic ease-out (`1 - (1-t)³`). Includes a six-up feature grid, three testimonial cards, a conversion CTA section, and a four-column footer.

---


## UI/UX Design Decisions

**Dark mode by default — not as a feature toggle.** The entire color system is built on a near-black void (`#020408`) with layered surface values (`#060c14` → `#0a1220` → `#0f1a2e`). This is not a light-mode app with an inverted stylesheet; the depth and hierarchy depend on this palette.

**A CSS custom property design system.** Every color, radius, and surface value is declared as a CSS variable in `:root`. There are no magic hex values scattered across 1,900 lines of code. The entire visual system can be re-skinned by changing twelve lines.

**Glassmorphism done with restraint.** Cards use `backdrop-filter: blur(12px)` with a semi-transparent background at 70% opacity. The effect is applied only to layered surfaces — sidebar, topbar, cards — not as an aesthetic default applied everywhere.

**Aurora backgrounds that don't burn CPU.** The animated gradient orbs are pure CSS pseudo-elements. No JavaScript, no Canvas, no requestAnimationFrame. They animate on the GPU.

**Interactive feedback on every element.** Cards lift 2px on hover with a border brightening and a linear-gradient highlight appearing along their top edge. Nav items have a left-edge accent bar when active. Buttons shift upward with increased box-shadow on hover. None of these use a JS event listener — they're all `:hover` pseudo-classes with CSS `transition`.

**Typography hierarchy.** Inter is used at weights from 300 to 900 across a seven-level type scale. JetBrains Mono appears exclusively on code identifiers, repo names, and monospace data. The display size (`clamp(40px, 7vw, 88px)`) scales fluidly across viewport widths without a single media query breakpoint.

**Responsive layout without a framework.** The sidebar collapses to 64px on desktop and slides off-canvas on mobile using CSS `transform`. The main content area shifts via `margin-left` with a matching `transition`. Grid layouts use `repeat(auto-fill, minmax())` where column count should adapt, and explicit `grid-template-columns` where the layout is intentional. A single breakpoint at 900px handles the mobile sidebar transition.

---

## Technology Stack

| Layer | Technology | Notes |
|---|---|---|
| UI Framework | React 18.2 (UMD) | Loaded via CDN; Babel standalone for JSX transpilation |
| Styling | Custom CSS Design System | ~500 lines of design tokens, components, and utilities |
| Rendering | HTML5 Canvas 2D API | Galaxy visualization — custom physics loop |
| Data Visualization | Hand-written SVG | Radar chart, score rings, constellation map |
| Animation | CSS Keyframes + `requestAnimationFrame` | Aurora, float, pulse, counter, heatmap |
| Intersection Observer API | Scroll-triggered counter animations | No scroll event listeners |
| Typography | Inter + JetBrains Mono (Google Fonts) | Variable weight loading |
| Viewport | CSS `clamp()` + CSS Grid | Fluid typography, responsive layout |

No build toolchain. No bundler. No Node.js required to run. Open the HTML file in a browser.

---

## Architecture

DevOS is a single-file React application. The architecture was designed for clarity and portability — a senior engineer should be able to understand the complete system by reading the file top to bottom.

```
devos.html
│
├── <style>                        CSS Design System
│   ├── :root                      Design tokens (colors, radii, shadows)
│   ├── Layout components          App shell, sidebar, topbar, main content
│   ├── UI primitives              Cards, buttons, badges, tags, progress bars
│   ├── Data visualization         Score rings, heatmap, constellation, radar
│   ├── Animation keyframes        Aurora, float, pulse, particle, shimmer
│   └── Responsive overrides       900px and 600px breakpoints
│
└── <script type="text/babel">     React Application
    ├── Data layer                 Static mock data (skills, repos, roadmap, etc.)
    ├── Primitive components       AnimatedCounter, ScoreRing, RadarChart, Heatmap
    ├── Signature components       GalaxyCanvas, ConstellationMap
    ├── Page components            Dashboard, SkillPage, ResumePage, GitHubPage,
    │                              RoadmapPage, InterviewPage, CareerPage
    ├── Layout components          Sidebar, Landing
    └── App root                   View state machine, page routing, sidebar state
```

**State management** is handled entirely with React's built-in `useState` and `useRef` hooks. There is no global state library. Each page component manages its own local state. The top-level `App` component owns three pieces of state: current view (`landing` or `app`), active page ID, and sidebar collapse state.

**Routing** is a simple string-keyed object map (`pageMap`) in the `App` component. Each key maps to a component instance, a title, and a subtitle. Switching pages is a single `setActivePage(id)` call with no URL changes — appropriate for a frontend-only demo.

**The Canvas animation loop** in `GalaxyCanvas` is initialized in a `useEffect` with a `useRef` to hold the animation frame ID. The cleanup function cancels the frame on unmount, preventing memory leaks. Node physics are computed in the draw function using simple Euler integration: position updates from velocity, velocity inverts on boundary collision.

---

## Folder Structure

For production extraction into a standard React project:

```
devos/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ui/
│   │   │   ├── ScoreRing.jsx          SVG ring with animated stroke-dashoffset
│   │   │   ├── RadarChart.jsx         SVG polar chart, hand-calculated geometry
│   │   │   ├── Heatmap.jsx            26-week contribution grid with CSS levels
│   │   │   ├── AnimatedCounter.jsx    IntersectionObserver + rAF counter
│   │   │   ├── ProgressBar.jsx        Gradient fill bar
│   │   │   ├── SkillBadge.jsx         Colored tier badge
│   │   │   └── Tag.jsx                Semantic color tag
│   │   ├── layout/
│   │   │   ├── Sidebar.jsx            Collapsible nav with active state
│   │   │   ├── Topbar.jsx             Sticky header with page title
│   │   │   └── AppShell.jsx           Root layout with aurora + grid overlay
│   │   ├── features/
│   │   │   ├── GalaxyCanvas.jsx       Canvas 2D physics visualization
│   │   │   └── ConstellationMap.jsx   SVG skill node map
│   │   └── landing/
│   │       ├── Hero.jsx               Hero section with floating cards
│   │       ├── Features.jsx           Six-up feature grid
│   │       ├── Testimonials.jsx       Social proof section
│   │       └── Footer.jsx             Four-column footer
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── SkillAnalyzer.jsx
│   │   ├── ResumeAnalyzer.jsx
│   │   ├── GitHubInsights.jsx
│   │   ├── GrowthRoadmap.jsx
│   │   ├── InterviewSimulator.jsx
│   │   └── CareerCommand.jsx
│   ├── data/
│   │   └── mockData.js                Skills, repos, roadmap, opportunities, testimonials
│   ├── styles/
│   │   ├── tokens.css                 CSS custom properties (design tokens)
│   │   ├── components.css             Card, button, badge, tag primitives
│   │   ├── layout.css                 App shell, sidebar, topbar, grid
│   │   ├── animations.css             Keyframes: aurora, float, pulse, shimmer
│   │   └── responsive.css             Breakpoints and mobile overrides
│   ├── hooks/
│   │   └── useIntersection.js         Reusable IntersectionObserver hook
│   ├── lib/
│   │   └── easing.js                  Cubic easing functions for counters
│   └── App.jsx                        View state machine and page routing
├── docs/
│   └── screenshots/
├── README.md
└── package.json
```

---

## Getting Started

No build step required.

**Option 1 — Open directly in browser**

```bash
git clone https://github.com/yourusername/devos.git
cd devos
open devos.html        # macOS
# or
start devos.html       # Windows
# or just drag the file into any modern browser
```

**Option 2 — Serve locally** (avoids CORS issues with font loading on some browsers)

```bash
# Python
python -m http.server 8080

# Node.js
npx serve .

# Then open http://localhost:8080/devos.html
```

**Requirements**

- Any modern browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- No Node.js, no npm, no build step
- Internet connection for Google Fonts (Inter + JetBrains Mono)

---

## Future Enhancements

**Real AI integration.** Connect skill gap analysis and roadmap generation to a language model API. The current prompt engineering for the interview feedback UI maps cleanly onto a `POST /v1/messages` call — the UI is already designed for streaming responses.

**Persistent state.** Replace static mock data with localStorage or IndexedDB so progress, roadmap state, and scores persist between sessions.

**GitHub OAuth.** The GitHub Insights page currently uses mock repo data. Connecting to the GitHub REST API (`/user/repos`, `/user/stats/contributions`) would make it genuinely useful.

**Resume PDF parsing.** The Resume Intelligence page currently scores static mock data. Integrating `pdf.js` to extract text from an uploaded PDF, then passing it to an LLM for section-by-section analysis, would complete the feature.

**Framer Motion upgrade.** Several animations (skill node entrance, card stagger, roadmap timeline reveal) would benefit from Framer Motion's layout animation and `AnimatePresence` for mount/unmount transitions. The current CSS approach is sufficient but has limits.

**Data visualization library migration.** The hand-written SVG radar chart and Canvas galaxy are intentional for this project. For a production version, migrating to D3.js for the radar and Three.js for a genuine 3D galaxy visualization would significantly expand capability.

**Keyboard navigation and command palette.** The sidebar nav is click-only. Adding keyboard shortcuts (e.g., `G then D` for Dashboard, following Linear's navigation model) and a `⌘K` command palette would meaningfully improve the power-user experience.

**Multi-user / team mode.** Career trajectory and skill benchmarking become significantly more useful when compared against peers. A team view showing skill distribution across a cohort would be a natural expansion.

---

## Design Inspiration

This project studied the following products closely:

**Linear** — Keyboard-first navigation, dense-but-not-cluttered information hierarchy, the "active nav item" left-edge accent bar pattern, and the principle that a tool used daily must be fast before it is beautiful.

**Stripe** — Documentation-level clarity in UI copy, precise use of color to communicate status (not just aesthetics), and the discipline of never showing a number without its unit and context.

**Vercel** — The dark-mode-first color system, the use of monospace type for technical identifiers, and the deployment status indicator pattern adapted here for roadmap node states.

**Notion** — Sidebar information architecture with collapsible sections, the idea that a workspace tool should feel like it has no wasted space, and breadcrumb-free navigation via clear page titles.

**Raycast** — The floating, glassmorphic panel aesthetic, the compact density of the command interface, and the principle that transitions should be fast (150–200ms) to feel responsive rather than decorative.

**Arc Browser** — The layered surface depth model, the aurora gradient background treatment, and the idea that a browser (or any daily tool) can feel genuinely joyful to open.

---

## Learning Outcomes

**Hand-rolling data visualizations.** Most projects reach for D3 or Recharts immediately. Building the radar chart, score rings, and galaxy visualization from first principles (SVG geometry, Canvas 2D API, trigonometry for polar coordinates) clarified exactly what abstraction layers those libraries provide — and when they're worth the dependency.

**CSS as a design system.** A disciplined `:root` custom property structure eliminates the need for a CSS-in-JS library in a frontend-only project. The cascade becomes a feature rather than a problem when the token system is consistent.

**Animation performance.** The distinction between GPU-composited properties (`transform`, `opacity`) and layout-triggering properties (`width`, `height`, `top`) is visible in practice when you have six simultaneous CSS animations and a 60fps Canvas loop running on the same page.

**`IntersectionObserver` for scroll effects.** Using `IntersectionObserver` instead of `scroll` event listeners for the animated counters avoids the main thread pressure of scroll handlers. The API is simple enough that a `useRef` + `useEffect` pattern is all that's needed — no library required.

**Single-file architecture as a constraint.** Building a complex UI in a single HTML file forces a discipline that component-heavy projects often skip: every component and style has to justify its existence, naming has to be consistent from the start, and there's no `../../../utils` escape hatch.

---

## AI-Assisted Development

This project was built with Claude (Anthropic) as the primary development partner.

The workflow was not "generate code, copy, paste." It was closer to pair programming with an architect who could draft at speed while I made structural decisions.

Specific areas where AI assistance was most effective:

**Design system architecture.** Working through the color token system — deciding which semantic names to use, how many surface levels to define, how opacity-based surfaces interact with the aurora background — before writing any component code.

**SVG geometry.** The radar chart requires trigonometry for polar-to-Cartesian coordinate conversion, grid polygon generation at multiple radii, and label positioning outside the outermost ring. Having a collaborator who could produce correct math on the first attempt and explain the derivation saved significant debugging time.

**Canvas physics.** The velocity vector initialization, boundary reflection logic, distance-based edge opacity calculation, and radial gradient node rendering in `GalaxyCanvas` were drafted collaboratively with iterative refinement on the visual output.

**Animation calibration.** Deciding animation durations, easing curves, and which elements should animate versus remain static. The `cubic-bezier(0.4, 0, 0.2, 1)` used on the sidebar collapse and the `1 - (1-t)³` easing on the counter animation were arrived at through iteration rather than guessing.

**Copy and content.** The landing page hero, feature descriptions, testimonial text, AI feedback copy, and coach insights are all written to match the voice and density of the target product category. Getting this right matters — generic placeholder copy undermines a premium visual design.

The final implementation reflects decisions and judgment that required a human in the loop. AI can draft; it cannot decide what the product should be.

---

