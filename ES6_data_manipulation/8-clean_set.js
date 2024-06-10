export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') return '';
  return [...set].reduce((acc, currentIndex) => {
    if (currentIndex.startsWith(startString)) return acc.concat(currentIndex.slice(startString.length), '-');
    return acc;
  }, '').slice(0, -1);
}
