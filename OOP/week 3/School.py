class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher


class teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course


class School:
    def __init__(self, name, students, courses, teachers):
        self.name = name
        self.students = students
        self.courses = courses
        self.teachers = teachers

    def get_students(self):
        for student in self.students:
            print(student.name)


school_name = 'Phitron'
ds_course = Course('Data Structure', 'POM')
pom_teacher = teacher('POM', ds_course)
algo_course = Course('Algorithm', 'Farzana')
farzana_teacher = teacher('POM', algo_course)

student_1 = Student(1, 'ellin', 20)
student_2 = Student(2, 'polin', 19)
student_3 = Student(3, 'jolin', 18)


teachers = [pom_teacher, farzana_teacher]
courses = [ds_course, algo_course]
students = [student_1, student_2, student_3]


my_school = School(school_name, students, courses, teachers)
print(my_school.name)
print(my_school.get_students())
