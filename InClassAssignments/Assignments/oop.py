class Dummy:
    pass

class NotDummy:
    #print('Hello World')
    #instance variable
    pi = 3.14
    grade = 0
    name = ""
    #constructor
    def __init__(self, a, b):
        self.grade = a
        self.name = b

    #mutator and accessor

    def set_grade(self, newGrade):
        self.grade = newGrade

    def get_grade(self):
        return self.grade

    #instance method
    def close(self):
        print('I am closing')

    def greeting(self, g):
        print('Your grade was: ', self.get_grade())
        self.set_grade(0)
        print('I decreased your grade to: ', self.grade, ' Congrats...You suck')
        print(g, self.name)
        self.close()

    #def greeting(self, g, c):
        #print(g, self.name, c)

#p1 = NotDummy(100, 'Saikat')
#p1.greeting('Hello')
#p1.greeting('Hello', 'Thank you!')

class Student(NotDummy):
    gradYr = 2021
    def __init__(self, grade, name, grad):
        #super().__init__(grade, name)
        NotDummy.__init__(self, grade, name)
        self.gradYr = grad

stu1 = Student(100, 'Saikat', 2021)
print(stu1.grade, stu1.name)


obj1 = NotDummy(23, 'Saikat')
obj2 = NotDummy(100, 'Das')
oldGrade = obj1.get_grade()
print('Your grade was: ', oldGrade)
obj1.set_grade(oldGrade+10)
print('Your current grade is: ', obj1.grade)
g = "hello"
print(obj1.name, obj1.grade)
print(obj2.name, obj2.grade)
obj1.greeting(g)
obj1.close()