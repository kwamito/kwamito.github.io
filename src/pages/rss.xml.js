import rss from '@astrojs/rss';
import { site as profile } from '../config/site';
import { getPublishedPosts } from '../lib/content';

export async function GET(context) {
  const posts = await getPublishedPosts();

  return rss({
    title: `Writing — ${profile.shortName}`,
    description: `Notes on backend engineering from ${profile.name}, ${profile.role} in ${profile.location}.`,
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
