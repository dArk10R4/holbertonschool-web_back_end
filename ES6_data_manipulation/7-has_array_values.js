export default function hasValuesFromArray(set, array) {
  return ([...set].toString() === [...new Set([...set, ...array])].toString());
}
