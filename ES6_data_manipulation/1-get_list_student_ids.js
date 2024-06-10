export default function getListStudentIds(arr) {
  try { return arr.map((it) => it.id); } catch (e) { return []; }
}
