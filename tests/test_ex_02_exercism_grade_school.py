from training_exercises.ex_02_exercism_grade_school import School


def test_roster_is_empty_when_no_student_is_added() -> None:
    school = School()
    expected: list[str] = []
    assert expected == school.roster()


def test_add_a_student() -> None:
    school = School()
    school.add_student(name="Aimee", grade=2)
    expected: list[bool] = [True]
    assert expected == school.added()


def test_student_is_added_to_the_roster() -> None:
    school = School()
    school.add_student(name="Aimee", grade=2)
    expected: list[str] = ["Aimee"]
    assert expected == school.roster()


def test_adding_multiple_students_in_the_same_grade_in_the_roster() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    expected: list[bool] = [True, True, True]
    assert expected == school.added()


def test_multiple_students_in_the_same_grade_are_added_to_the_roster() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    expected: list[str] = ["Blair", "James", "Paul"]
    assert expected == school.roster()


def test_cannot_add_student_to_same_grade_in_the_roster_more_than_once() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    expected: list[bool] = [True, True, False, True]
    assert expected == school.added()


def test_student_not_added_to_same_grade_in_the_roster_more_than_once() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    expected: list[str] = ["Blair", "James", "Paul"]
    assert expected == school.roster()


def test_adding_students_in_multiple_grades() -> None:
    school = School()
    school.add_student(name="Chelsea", grade=3)
    school.add_student(name="Logan", grade=7)
    expected: list[bool] = [True, True]
    assert expected == school.added()


def test_students_in_multiple_grades_are_added_to_the_roster() -> None:
    school = School()
    school.add_student(name="Chelsea", grade=3)
    school.add_student(name="Logan", grade=7)
    expected: list[str] = ["Chelsea", "Logan"]
    assert expected == school.roster()


def test_cannot_add_same_student_to_multiple_grades_in_the_roster() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=3)
    school.add_student(name="Paul", grade=3)
    expected: list[bool] = [True, True, False, True]
    assert expected == school.added()


def test_student_not_added_to_multiple_grades_in_the_roster() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=3)
    school.add_student(name="Paul", grade=3)
    expected: list[str] = ["Blair", "James", "Paul"]
    assert expected == school.roster()


def test_students_are_sorted_by_grades_in_the_roster() -> None:
    school = School()
    school.add_student(name="Jim", grade=3)
    school.add_student(name="Peter", grade=2)
    school.add_student(name="Anna", grade=1)
    expected: list[str] = ["Anna", "Peter", "Jim"]
    assert expected == school.roster()


def test_students_are_sorted_by_name_in_the_roster() -> None:
    school = School()
    school.add_student(name="Peter", grade=2)
    school.add_student(name="Zoe", grade=2)
    school.add_student(name="Alex", grade=2)
    expected: list[str] = ["Alex", "Peter", "Zoe"]
    assert expected == school.roster()


def test_students_are_sorted_by_grades_and_then_by_name_in_the_roster() -> None:
    school = School()
    school.add_student(name="Peter", grade=2)
    school.add_student(name="Anna", grade=1)
    school.add_student(name="Barb", grade=1)
    school.add_student(name="Zoe", grade=2)
    school.add_student(name="Alex", grade=2)
    school.add_student(name="Jim", grade=3)
    school.add_student(name="Charlie", grade=1)
    expected: list[str] = ["Anna", "Barb", "Charlie", "Alex", "Peter", "Zoe", "Jim"]
    assert expected == school.roster()


def test_grade_is_empty_if_no_students_in_the_roster() -> None:
    school = School()
    expected: list[str] = []
    assert expected == school.grade(1)


def test_grade_is_empty_if_no_students_in_that_grade() -> None:
    school = School()
    school.add_student(name="Peter", grade=2)
    school.add_student(name="Zoe", grade=2)
    school.add_student(name="Alex", grade=2)
    school.add_student(name="Jim", grade=3)
    expected: list[str] = []
    assert expected == school.grade(1)


def test_student_not_added_to_same_grade_more_than_once() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="Paul", grade=2)
    expected: list[str] = ["Blair", "James", "Paul"]
    assert expected == school.grade(2)


def test_student_not_added_to_multiple_grades() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=3)
    school.add_student(name="Paul", grade=3)
    expected: list[str] = ["Blair", "James"]
    assert expected == school.grade(2)


def test_student_not_added_to_other_grade_for_multiple_grades() -> None:
    school = School()
    school.add_student(name="Blair", grade=2)
    school.add_student(name="James", grade=2)
    school.add_student(name="James", grade=3)
    school.add_student(name="Paul", grade=3)
    expected: list[str] = ["Paul"]
    assert expected == school.grade(3)


def test_students_are_sorted_by_name_in_a_grade() -> None:
    school = School()
    school.add_student(name="Franklin", grade=5)
    school.add_student(name="Bradley", grade=5)
    school.add_student(name="Jeff", grade=1)
    expected: list[str] = ["Bradley", "Franklin"]
    assert expected == school.grade(5)
