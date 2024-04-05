
def gradingStudents(grades):

    new_grades = []

    for grade in grades:
        print(f"New: {grade%5}")
        if grade >= 38 and grade % 5 > 2:
            new_grades.append(grade + (5-grade%5))
        else:
            new_grades.append(grade)

    return new_grades



if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
