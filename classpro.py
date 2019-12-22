#class for student access
class database():
    print("students details")
    def __init__(self,stu_name,pas_word,marks,aver):
        self.stu_name=stu_name
        self.pas_word=pas_word
        self.marks=marks
        self.aver=aver

    def student(self,pwd):
        print("Hi" + self.stu_name + "enter your password")
        if self.pas_word==pwd:
            print("your password is correct")
            wrt=open('test.txt','w')
            print("your marks are")
            print(wrt.write(self.marks))

        else:
            print("incorrect password try again later")
            
access=database("athmika",12345,"90",67)
access.student(12345)
    
            
        
