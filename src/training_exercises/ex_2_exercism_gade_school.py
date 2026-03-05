"""
Instructions
Given students' names along with the grade they are in, create a roster for the school.

In the end, you should be able to:

Add a student's name to the roster for a grade:
"Add Jim to grade 2."
"OK."
Get a list of all students enrolled in a grade:
"Which students are in grade 2?"
"We've only got Jim right now."
Get a sorted list of all students in all grades. Grades should be sorted as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
"Who is enrolled in school right now?"
"Let me think. We have Anna, Barb, and Charlie in grade 1, Alex, Peter, and Zoe in grade 2, and Jim in grade 5. So the answer is: Anna, Barb, Charlie, Alex, Peter, Zoe, and Jim."
Note that all our students only have one name (it's a small town, what do you want?), and each student cannot be added more than once to a grade or the roster. If a test attempts to add the same student more than once, your implementation should indicate that this is incorrect.

The tests for this exercise expect your school roster will be implemented via a School class in Python. If you are unfamiliar with classes in Python, classes from the Python docs is a good place to start.

"""


class School:
    """Manage a school roster of students organized by grade.

    This class tracks student names and their respective grades, preventing
    duplicate enrollments and providing methods to query the roster by grade
    or retrieve all students in sorted order.
    """

    def __init__(self) -> None:
        """Initialize an empty school roster."""
        self._students: dict[str, int] = {}
        self._add_status: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the roster for a given grade.

        If the student already exists in the roster, the addition is rejected.
        The result of each add attempt is tracked in the add status history.

        Args:
            name (str): the name of the student
            grade (int): the grade level for enrollment
        """
        if name in self._students:
            self._add_status.append(False)
        else:
            self._students[name] = grade
            self._add_status.append(True)

    def roster(self) -> list[str]:
        """Return a sorted list of all students in all grades.

        Students are sorted first by grade (ascending), then alphabetically
        by name within each grade.

        Returns:
            list[str]: names of all students, sorted as described above
        """
        sorted_students = sorted(
            self._students.items(), key=lambda item: (item[1], item[0])
        )
        return [student_name for student_name, _ in sorted_students]

    def grade(self, grade_number: int) -> list[str]:
        """Return all students in a specific grade, sorted alphabetically.

        Args:
            grade_number (int): the grade to query

        Returns:
            list[str]: names of all students in that grade, sorted alphabetically
        """
        students_in_grade = [
            student_name
            for student_name, student_grade in self._students.items()
            if student_grade == grade_number
        ]
        return sorted(students_in_grade)

    def added(self) -> list[bool]:
        """Return the history of add attempts.

        Returns:
            list[bool]: a list where each True indicates a successful addition
                and False indicates a rejected duplicate
        """
        return self._add_status
