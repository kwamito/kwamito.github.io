import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    problem: z.string(),
    impact: z.string(),
    tags: z.array(z.string()),
    order: z.number().default(99),
    /** Your role on the project, e.g. "Lead Backend Engineer". */
    role: z.string().optional(),
    /** Free-form timeframe, e.g. "2023 — 2024". */
    period: z.string().optional(),
    /** Headline outcomes. Only facts stated in the case study. */
    metrics: z.array(z.object({ value: z.string(), label: z.string() })).default([]),
    /** Core technologies, shown in the metadata rail. Falls back to `tags`. */
    stack: z.array(z.string()).optional(),
    /** External links (repo, live site, write-up). */
    links: z
      .array(z.object({ label: z.string(), href: z.url().or(z.string().startsWith('/')) }))
      .default([]),
    /** Optional screenshots (e.g. mobile screens), served from public/. */
    screenshots: z.array(z.object({ src: z.string().startsWith('/'), alt: z.string() })).optional(),
  }),
});

const writing = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, writing };
