# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static website project for Staks Rosch, featuring a 100-page website covering his work as an atheist activist, writer, philosopher, and musician. The project uses Python scripts to generate HTML pages and deploys to GitHub Pages.

**Key characteristics:**
- Static HTML website (no backend or framework)
- Python-based page generation scripts
- Manual content management (no CMS)
- GitHub Pages deployment via GitHub Actions
- Swiss/Editorial design style with responsive layout

## Repository Structure

```
/
├── staks-rosch-website/        # Generated static website output
│   ├── index.html              # Homepage
│   ├── sitemap.html            # Site navigation
│   ├── css/main.css            # Complete stylesheet
│   ├── js/main.js              # Navigation and interactions
│   ├── biography/              # 10 pages
│   ├── book/                   # 13 pages
│   ├── activism/               # 15 pages
│   ├── writings/               # 20 pages
│   ├── philosophy/             # 15 pages
│   ├── music/                  # 10 pages
│   ├── resources/              # 10 pages
│   └── blog/                   # 6 pages
├── create_pages.py             # Initial page generation script
├── generate_website.py         # Page generation template system
├── generate_all_pages.py       # Batch page creation script
├── update_pages.py             # Script for updating specific pages
└── .github/workflows/deploy.yml # GitHub Pages deployment
```

## Development Commands

### Generate Website Pages

The website is generated using Python scripts. There are three main generation scripts:

```bash
# Generate all pages (creates complete 100-page website)
python3 generate_all_pages.py

# Alternative generation script (template-based approach)
python3 generate_website.py

# Initial page creation script
python3 create_pages.py

# Update specific pages with enhanced content
python3 update_pages.py
```

**Important:** These scripts write to `/workspace/staks-rosch-website/` in the scripts. If running locally, you may need to update the `base_dir` variable to match your file system path:
```python
base_dir = Path("/Users/chalizardking/Downloads/package (7)/staks-rosch-website")
```

### Deployment

The site automatically deploys to GitHub Pages on push to main:

```bash
# Deploy happens automatically via GitHub Actions
git add .
git commit -m "Update website content"
git push origin main
```

Manual deployment can also be triggered via GitHub Actions UI using workflow_dispatch.

### Local Development

To view the website locally:

```bash
# Navigate to the website directory
cd staks-rosch-website

# Serve with Python's built-in HTTP server
python3 -m http.server 8000

# Or use any static file server
# npx serve .
# php -S localhost:8000
```

Then open http://localhost:8000 in your browser.

## Architecture & Design Patterns

### Page Generation System

The website uses a **template-based generation pattern** where Python functions create HTML pages from structured data:

1. **Template Functions**: `create_html_page()` or `create_page()` functions accept parameters (title, category, content) and output complete HTML files
2. **Data-Driven Content**: Page definitions are stored as Python lists/dicts containing metadata and content
3. **Consistent Structure**: All pages share navigation, hero sections, and footer via templating
4. **File Organization**: Pages are organized by topic into subdirectories matching site sections

### Key Generation Pattern

```python
def create_html_page(title, category, hero_title, subtitle, content, filepath, level="../"):
    # Builds complete HTML with:
    # - Navigation with relative paths
    # - Hero section with category/title/subtitle
    # - Main content area
    # - Footer with links
    # - JavaScript includes
```

### Design System

The site follows a **Swiss/Editorial design philosophy**:

- **Typography**: Inter (headings) + Crimson Pro (body text)
- **Grid System**: 8px base grid for consistent spacing
- **Color Palette**: Primary blue (#2A4B7C), neutral grays, semantic colors
- **Layout**: Max 1280px container, 720px content column for readability
- **Responsive**: Breakpoints at 768px (tablet) and 1024px (desktop)

### Navigation Architecture

- **Sticky header navigation** across all pages
- **Hamburger menu** for mobile devices (JS-powered toggle)
- **Footer navigation** organized by topic categories
- **Relative path handling** via `level` parameter (adjusts `../` depth)

## Content Management

### Adding New Pages

To add new pages to existing sections:

1. Add page definition to appropriate list in `generate_all_pages.py`:
```python
("filename", "Title", "Subtitle")
```

2. Regenerate the site:
```bash
python3 generate_all_pages.py
```

### Creating New Sections

To create an entirely new section:

1. Add section to navigation in template functions
2. Create new topic list with page definitions
3. Add generation loop for the new section
4. Update footer navigation
5. Regenerate site

### Updating Existing Content

For targeted updates without full regeneration:

1. Edit content in `update_pages.py`
2. Run the update script:
```bash
python3 update_pages.py
```

Or manually edit HTML files in `staks-rosch-website/` directory.

## Important Notes & Conventions

### Path Handling

All generation scripts use absolute paths that assume `/workspace/` base directory. When working locally, update `base_dir` variables to match your actual file system location.

### HTML Structure Convention

Every page follows this structure:
1. `<head>` with title, meta tags, CSS link
2. `<nav>` with site-wide navigation
3. `<section class="hero">` for page header
4. `<main class="container">` for content
5. `<footer>` with multi-column navigation
6. `<script>` for JavaScript

### CSS Architecture

The `main.css` file uses:
- CSS custom properties (variables) for theming
- Mobile-first responsive approach
- Utility classes for common patterns
- Semantic class naming (`.hero-title`, `.content-section`)

### JavaScript Functionality

The `main.js` handles:
- Mobile navigation toggle
- Active navigation link highlighting
- Smooth scroll for anchor links
- Optional scroll progress indicator

### Content Philosophy

Content is based on publicly available information about Staks Rosch including:
- His book "Disproving God and 5 Adequate Reasons To Be an Atheist"
- HuffPost articles and blog posts
- Philadelphia Coalition of Reason activism
- Publishers Weekly interviews
- DangerousTalk blog archives

### GitHub Pages Deployment

The `.github/workflows/deploy.yml` workflow:
1. Triggers on push to main or manual dispatch
2. Checks out repository
3. Configures GitHub Pages
4. Uploads `staks-rosch-website/` directory as artifact
5. Deploys to GitHub Pages environment

No build step is required since pages are pre-generated HTML.

## Codacy Integration

This project has Codacy MCP Server integration configured via `.windsurfrules`. After editing files, the Codacy CLI analyzer runs automatically to check for code quality issues and security vulnerabilities.

Key rules:
- Analyze files after edits using `codacy_cli_analyze`
- Security scan with Trivy after dependency changes
- Propose and apply fixes for issues found
