class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade        
class course:
    def __init__(self, name, maxstudents):
        self.name = name
        self.maxstudents = maxstudents
        self.students = []
    def add_student(self, student):
        if len(self.students)< self.maxstudents:
            self.students.append(student)
        return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)
s1 = student("TIM", 19, 99)
s2 = student("BILL", 18, 78)
s3 = student("kristjan", 19, 55)
course = course("science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[1].name)
print(course.get_average_grade())