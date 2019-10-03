#类
from c4 import Human

class Student(Human):

    def __init__(self,school,name,age):
        self.school=school
        # Human.__init__(self,name,age)
        super(Student,self).__init__(name,age)

    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))
    
student = Student('aaa','xrr',16)
student1 = Student('bbb','xrrr',16)
student.print_file()
print(student.name)
print(Student.sum)
print(student1.sum)
student.get_name()