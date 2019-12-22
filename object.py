class Management():
    print("password checking")


    def check(self,username,password):
        self.username=username
        self.password=password
        
        if self.username=="abhi" and self.password==9393:
            print("login successfull")
            return True
        else:
            print("wrong password")
            return False

pas=Management("abhi",9393)
pas.check(3939,"amulu")
#pas.check(9393,"abhi")

''''class Student(Management):
    def __init__(self,username,password,standard,marks):
        self.standard=standard
        self.marks=marks

        login_status=super(Student,self).check(username,password)
        if login_status:
            self.show_mark()
            
    def show_mark(self):
        print(self.marks)

student1=Student("abhi",9393,10,[1,2,3,4,5])'''

                  
