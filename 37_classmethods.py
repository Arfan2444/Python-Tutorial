# class methods - allow operations related to the class itself rather than instances
#                 Take (cls) as the first parameter, which represents the class itself


class Student:
    
    count = 0
    totalgpa = 0.0

    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.totalgpa += gpa
    
    def getinfo(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")
    
    @classmethod
    def countstudents(cls):
        print(f"Total Students: {cls.count}")

    @classmethod
    def averagegpa(cls):
        if cls.count == 0:
            print("No students to calculate average GPA.")
        else:
            avg = cls.totalgpa / cls.count
            print(f"Average GPA: {avg:.2f}")

student1 = Student("Spongebob", 3.5)
student2 = Student("Patrick", 2.0)
student3= Student("Sandy", 4.0)

student1.getinfo()
student2.getinfo()
student3.getinfo()

Student.countstudents()
Student.averagegpa()