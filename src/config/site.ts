// Single source for identity, contact details and profile links.
// Anything left `null` is hidden from the site instead of rendering a dead link.
export interface SiteConfig {
  name: string;
  shortName: string;
  role: string;
  location: string;
  timeZone: string;
  availability: string;
  email: string | null;
  github: string | null;
  linkedin: string | null;
  cv: string | null;
  formspreeId: string | null;
}

export const site: SiteConfig = {
  name: 'Nana Kwame Oparrey Kuhney',
  shortName: 'Nana Kwame',
  role: 'Lead Backend Engineer',
  location: 'Accra, Ghana',
  timeZone: 'Africa/Accra',
  availability: 'Open to senior backend roles and contracts',

  email: 'kuhneykwame@gmail.com',
  github: 'https://github.com/kwamito',
  linkedin: 'https://www.linkedin.com/in/kwame-kuhney/',
  cv: null, // TODO: set to '/cv.pdf' once public/cv.pdf exists

  // TODO: create a form at https://formspree.io and paste its ID here. The form is hidden until set.
  formspreeId: null,
};

export const displayUrl = (url: string) => url.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, '');
