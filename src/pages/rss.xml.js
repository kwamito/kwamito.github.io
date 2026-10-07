import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { site as profile } from '../config/site';

export async function GET(context) {
  const posts = (await getCollection('writing', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.date.valueOf() - a.data.date.valueOf(),
  );

  return rss({
    title: `Writing — ${profile.shortName}`,
    description: `Notes on backend engineering from ${profile.name}, Lead Backend Engineer in ${profile.location}.`,
    site: context.site,
    trailingSlash: true,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.date,
      link: `/writing/${post.id}/`,
      categories: post.data.tags,
    })),
    customData: '<language>en</language>',
  });
}
