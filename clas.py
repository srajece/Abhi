#class with constructor
#class with constructor
class database():
    print("modern school")
    def __init__(self,name,clas,
                 rno,marks,
                 attendance,fees):
        self.name=name
        self.clas=clas
        self.rno=rno
        self.marks=marks
        self.attendance=attendance
        self.fees=fees

        
    def staff(self):
        print("student name:",self.name)
        print("register number:",self.rno)

    def showmark(self):
        print("subject marks:",self.marks)

        
    def student(self):
        print("your name:",self.name)
        print("your marks",self.marks)


    def management(self):
        print("student name:",self.name)
        print("register number:",self.rno)
        print("fees remaining",self.fees)
        print("attendance percentage",self.attendance)
    


school=database("athmika","LKG",298,95,"90%",1000)
school.staff()
school.student()
school.management()















































'''#sub classes
class NewCalc(OldCalc):
    def muplication(self):
        c=self.a*self.b
        print(c)
    def division(self):
        c=self.a/self.b
        print(c)
class ModernCalc(NewCalc):
    def modulus(self):
        c=self.a%self.b
        print(c)
ModernCalc.addition(20,30)
ModernCalc.modulus(81,5)
ModernCalc.division(81,5)
calc=ModernCalc(10,20)
calc.modulus()
calc.division()
calc.muplication()

#class without constructor
class OldCalc:
def addition(a,b):
        c=a+b
        print(c)
    def subtraction(a,b):
        c=a-b
        print(c)
#sub classes
class NewCalc(OldCalc):
    def muplication(a,b):
        c=a*b
        print(c)
    def division(a,b):
        c=a/b
        print(c)
class ModernCalc(NewCalc):
    def modulus(a,b):
        c=a%b
        print(c)'''

