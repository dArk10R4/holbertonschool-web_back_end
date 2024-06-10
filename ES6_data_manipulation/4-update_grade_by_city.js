export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const modified = student;
    try { modified.grade = newGrades.filter((grade) => grade.studentId === modified.id)[0].grade; } catch (e) { modified.grade = 'N/A'; }
    return modified;
  });
}
