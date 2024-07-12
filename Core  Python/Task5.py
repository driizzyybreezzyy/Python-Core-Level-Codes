class StudentInfo:
    def __init__(self, stu_rno, stu_name):
        self.stu_rno = stu_rno
        self.stu_name = stu_name

class StudentMarks:
    def __init__(self, stu_rno, stu_m1, stu_m2, stu_m3):
        self.stu_rno = stu_rno
        self.stu_m1 = stu_m1
        self.stu_m2 = stu_m2
        self.stu_m3 = stu_m3

class MainClass:
    def __init__(self):
        self.students = []

    def get_info(self):
        n = int(input("Enter no of students : "))
        for i in range(n):
            rno = input(f"Enter Roll no of Student {i + 1} : ")
            name = input(f"Enter Name of student {i + 1} : ")
            student_info = StudentInfo(rno, name)
            self.students.append(student_info)

    def get_marks(self):
        for student in self.students:
            rno = student.stu_rno
            m1 = int(input(f"Enter Marks 1 for student {rno} :"))
            m2 = int(input(f"Enter Marks 2 for student {rno} :"))
            m3 = int(input(f"Enter Marks 3 for student {rno} :"))
            student_marks = StudentMarks(rno, m1, m2, m3)
            student.student_marks = student_marks

    def cal_avg(self):
        for student in self.students:
            rno = student.stu_rno
            m1 = student.student_marks.stu_m1
            m2 = student.student_marks.stu_m2
            m3 = student.student_marks.stu_m3
            average = (m1 + m2 + m3) / 3
            grade = calculate_grade(average)
            print(f"Average marks for student {rno}: {average}")
            print(f"Grade for student {rno}: {grade}")

from Task5 import StudentInfo, StudentMarks, MainClass
from grade_calculator import calculate_grade

main = MainClass()
main.get_info()
main.get_marks()
main.cal_avg()
