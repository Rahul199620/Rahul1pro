class student:
     def __init__(self):
         print("our class is created")
     def __del__(self):
        print("our class is destroyed")
     def setmyname(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

     def printname(self):
         print(self.firstname,"",self.lastname,self.age)


name=student()
name.setmyname('shivam','walia',25)
name.printname()


