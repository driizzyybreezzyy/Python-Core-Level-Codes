n = int(input("Enter the number of students: "))
def write_data(n):
    with open("studentInfo.txt", "w") as info_file:
        for i in range(n):
            rollno = input("Enter roll number for student: ")
            name = input("Enter name for student {}: ".format(i+1))
            info_file.write("{}-{}\n".format(rollno, name))

    with open("studentMarks.txt", "w") as marks_file:
        for i in range(n):
            marks = input("Enter marks for student {} (separated by ,): ".format(i+1))
            marks_file.write("{}-{}\n".format(rollno, marks))

def calculate_grade():
    with open("studentMarks.txt", "r") as marks_file:
        marks_data = marks_file.readlines()
    grade_data = []

    for line in marks_data:
        print(line)
        rollno, marks = line.strip().split("-")
        marks = list(map(int, marks.split(",")))
        average_grade = sum(marks) / len(marks)
        if average_grade > 80:
            grade = "A"
        elif average_grade > 60 or average_grade <= 80:
            grade = "B"
        elif average_grade >= 40 or average_grade <= 60:
            grade = "C"
        else:
            grade = "D"
        # grade_data[rollno] = grade
        grade_data.append([rollno,grade])
        print(grade_data)
        grade_data=dict(grade_data)
        print(grade_data)
    with open("grade.txt", "a+") as grade_file:
        # print(grade_data)
        for rollno, grade in grade_data.items():
            grade_file.write("{}-{}\n".format(rollno, grade))

write_data(n)
calculate_grade()