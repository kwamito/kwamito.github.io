type Falsy = false | null | undefined | '' | 0;

/** Drops falsy entries with a proper type guard, so no cast is needed after filtering. */
export function compact<T>(arr: (T | Falsy)[]): T[] {
  return arr.filter((x): x is T => Boolean(x));
}
