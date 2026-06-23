# Nana Kwame Oparrey Kuhney — Portfolio

Personal portfolio site for Nana Kwame Oparrey Kuhney, backend engineer based in Ghana.

Built with **Astro 7**, **Tailwind CSS 4**, **MDX**, and **TypeScript**. Fully static output.

---

## Commands

```sh
npm install         # install dependencies
npm run dev         # start dev server at http://localhost:4321
npm run build       # build production site to ./dist/
npm run preview     # preview the production build locally
```

---

## Adding a Blog Post

1. Create a new `.mdx` file in `src/content/writing/`:

```
src/content/writing/my-new-post.mdx
```

2. Add frontmatter at the top:

```yaml
---
title: "Your Post Title"
description: "A one-sentence summary for SEO and previews."
date: 2024-06-01
tags: ["Django", "PostgreSQL"]   # optional
draft: false                      # set true to hide from listings
---
```

3. Write your content below the frontmatter using Markdown.

The post will be available at `/writing/my-new-post/` and appear on the writing index automatically.

---

## Adding or Updating Projects / Case Studies

1. Create or edit a `.mdx` file in `src/content/projects/`:

```
src/content/projects/my-project.mdx
```

2. Frontmatter schema:

```yaml
---
title: "Project Title"
description: "Short description for the card view."
problem: "One sentence describing the core problem."
impact: "One sentence describing measurable outcome."
tags: ["Python", "Django", "PostgreSQL"]
order: 1          # controls sort order on /projects (lower = first)
featured: true    # shows on the homepage
---
```

3. Write the full case study in the body.

The project will appear at `/projects/my-project/` and on the `/projects` index.

---

## Where to Update Personal Links

| What | File |
|------|------|
| GitHub URL | `src/components/layout/Footer.astro` + `src/pages/contact.astro` |
| LinkedIn URL | `src/components/layout/Footer.astro` + `src/pages/contact.astro` |
| Email address | `src/components/layout/Footer.astro` + `src/pages/contact.astro` |
| CV/Resume PDF | Add `cv.pdf` to `public/cv.pdf` — link is already in `/experience` and `/contact` |
| Site URL (for sitemap/OG) | `astro.config.mjs` → `site` field + `src/components/layout/Layout.astro` |
| About page bio | `src/pages/about.astro` |
| Experience details | `src/pages/experience.astro` |
| Contact availability status | `src/pages/contact.astro` |

---

## Project Structure

```
src/
├── components/
│   ├── layout/
│   │   ├── Layout.astro        # Base HTML layout (SEO, fonts, theme)
│   │   ├── Navbar.astro        # Fixed top nav + mobile menu
│   │   └── Footer.astro        # Footer with social links
│   ├── ui/
│   │   ├── ThemeToggle.astro   # Dark/light mode toggle
│   │   ├── SectionHeading.astro
│   │   └── Badge.astro         # Tech tag badge
│   ├── home/
│   │   ├── Hero.astro          # Hero section with API response visual
│   │   ├── StatsStrip.astro    # 4-stat highlights strip
│   │   └── CTASection.astro    # Call-to-action section
│   ├── ProjectCard.astro
│   ├── BlogCard.astro
│   ├── SkillCard.astro
│   └── ExperienceTimeline.astro
├── content/
│   ├── projects/               # MDX case studies
│   └── writing/                # MDX blog posts
├── pages/
│   ├── index.astro             # Home
│   ├── about.astro
│   ├── experience.astro
│   ├── skills.astro
│   ├── contact.astro
│   ├── projects/
│   │   ├── index.astro
│   │   └── [...slug].astro     # Dynamic case study pages
│   ├── writing/
│   │   ├── index.astro
│   │   └── [...slug].astro     # Dynamic blog post pages
│   └── robots.txt.ts
├── styles/
│   └── global.css              # Tailwind + design tokens
└── content.config.ts           # Content collection schemas
```

---

## Theme

Dark mode is class-based (`.dark` on `<html>`). The theme toggle persists to `localStorage` and respects `prefers-color-scheme` on first visit. The toggle script runs inline in `<head>` to prevent flash of wrong theme.

---

## Deploying

The site outputs to `./dist/` as plain HTML/CSS/JS — deployable to any static host:

- **Netlify**: connect repo, build command `npm run build`, publish dir `dist`
- **Vercel**: same — auto-detected as Astro
- **GitHub Pages**: use the Astro GitHub Pages action
- **Cloudflare Pages**: connect repo, framework preset: Astro

Update `site` in `astro.config.mjs` to your final domain before deploying (required for sitemap and OG image URLs).
