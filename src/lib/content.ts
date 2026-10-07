import { getCollection } from 'astro:content';

/** Estimated reading time in minutes at ~200 words per minute (minimum 1). */
export function readingTime(body: string): number {
  const words = body.split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.ceil(words / 200));
}

const dateFormats = {
  /** "05 Sept 2023" — post cards. */
  short: { day: '2-digit', month: 'short', year: 'numeric' },
  /** "5 September 2023" — post header. */
  long: { day: 'numeric', month: 'long', year: 'numeric' },
  /** "05 Sept" — writing index, where posts are already grouped by year. */
  dayMonth: { day: '2-digit', month: 'short' },
} satisfies Record<string, Intl.DateTimeFormatOptions>;

/** Content dates are calendar dates, so always format them in UTC. */
export function formatDate(d: Date, style: keyof typeof dateFormats): string {
  return d.toLocaleDateString('en-GB', { ...dateFormats[style], timeZone: 'UTC' });
}

/** All projects, ordered by their `order` field. */
export async function getSortedProjects() {
  const projects = await getCollection('projects');
  return projects.sort((a, b) => a.data.order - b.data.order);
}

/** Non-draft posts, newest first. */
export async function getPublishedPosts() {
  const posts = await getCollection('writing', ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}
