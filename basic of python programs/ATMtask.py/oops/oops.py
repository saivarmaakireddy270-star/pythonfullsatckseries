#oops variables
#instance variable
#class variable
#local variable
#instance variable
class student:
    college="anu"
    def talk(self):
        x=100
        self.name="raju"
        print("i am constructor")
        print("my name is",self.name)
        print("my college name is",student.college)
        print("my value is",x)
t=student()
student.college
t1=student()
t2=student()
t2.talk()

#class variable


        