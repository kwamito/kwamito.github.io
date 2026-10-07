// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://kwamito.github.io',
  output: 'static',
  markdown: {
    shikiConfig: {
      // Dual themes: colours are emitted as --shiki-light / --shiki-dark CSS
      // variables and switched in src/styles/prose.css based on the .dark class.
      themes: {
        light: 'github-light',
        dark: 'github-dark-dimmed',
      },
      defaultColor: false,
      wrap: false,
    },
  },
  vite: {
    plugins: [tailwindcss()],
  },
  integrations: [mdx(), sitemap()],
});