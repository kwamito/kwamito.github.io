// Whole-card click without overlaying the text: navigate via the card's single
// [data-card-link] unless the user is selecting text or clicked another
// interactive element. Imported by ProjectCard and BlogCard; Astro bundles the
// module once per page, so the listener is only bound once.
document.addEventListener('click', (e) => {
  const target = e.target as HTMLElement | null;
  const card = target?.closest<HTMLElement>('[data-card]');
  if (!card || target?.closest('a, button, input, select, textarea')) return;
  if (window.getSelection()?.toString()) return;
  const link = card.querySelector<HTMLAnchorElement>('[data-card-link]');
  if (!link) return;
  if (e.metaKey || e.ctrlKey) window.open(link.href, '_blank', 'noopener');
  else link.click();
});
