class Employee:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greating_the_person(self):
        print("Welcome " + self.fname)
emp1 = Employee("Yanko","Ribarski","abv")
print(emp1.email)
emp1.greating_the_person()