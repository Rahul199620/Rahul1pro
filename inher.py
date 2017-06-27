class detail:
    def myname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def cmname(self):
        print(self.firstname,"",self.lastname)

class stud(detail):
    def hsname(self,age,sex):
        self.age=age
        self.sex=sex
    def nm(self):
            print(self.age,"",self.sex)

obj1=stud()
obj1.myname("rahul","thakur")
obj1.cmname()
obj1.hsname(23,"male")
obj1.nm()




