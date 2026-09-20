class Person:

    def set_person_details(self, name, age):
        self.name = name
        self.age = age

class Course:

    def set_course_details(self, course, duration):
        self.course = course
        self.duration = duration

class Student(Person, Course):

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Duration:", self.duration)

student = Student()

student.set_person_details("Harini", 20)
student.set_course_details("CSE", "4 years")

student.display()
