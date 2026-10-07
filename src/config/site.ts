// Single source for contact details and profile links.
// Anything left `null` is hidden from the site instead of rendering a dead link.
export const site = {
  name: 'Nana Kwame Oparrey Kuhney',
  shortName: 'Nana Kwame',
  role: 'Backend Engineer',
  location: 'Accra, Ghana',
  timeZone: 'Africa/Accra',
  availability: 'Open to senior backend roles and contracts',

  email: 'kuhneykwame@gmail.com' as string | null,
  github: 'https://github.com/kwamito',
  linkedin: 'https://www.linkedin.com/in/kwame-kuhney/' as string | null,
  cv: null as string | null, // TODO: set to '/cv.pdf' once public/cv.pdf exists

  // TODO: create a form at https://formspree.io and paste its ID here. The form is hidden until set.
  formspreeId: null as string | null,
};

export const displayUrl = (url: string) => url.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, '');
