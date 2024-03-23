"""class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is {}.".format(self.id))

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I'm an admin")

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I'm a manager")

e1 = Employee()
e1.say_id()
e2 = Employee()
e3 = Admin()
e3.say_id()
e4 = Manager()
e4.say_id()

class Employee():
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1
    def say_id(self):
        print("My id is {}".format(self.id))

class User():
    def __init__(self,username,role="customer"):
        self.username = username
        self.role = role
    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))

class Admin(Employee,User):
    def __init__(self):
        super().__init__()
        User.__init__(self,self.id,"Admin")

e3 = Admin()
e3.say_user_info()

class Meeting():
    def __init__(self):
        self.attendees = []

    def __len__(self):
        return len(self.attendees)

    def __add__(self, Employee):
        print("ID {} added".format(Employee.id))
        self.attendees.append(Employee)

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))"""


#Abstraction meanse the class inheriting needs to use the abstracted function
"""from abc import ABC, abstractmethod
class AbstractEmployee(ABC):
    new_id = 1
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print("My id is {}".format(self.id))

e1 = Employee()
e1.say_id()"""



# __ : cant use outside the class
"""class Employee():
    new_id = 1
    def __init__(self,name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self,new_name):
        self._name = new_name

    def del_name(self):
        del self._name

e1 = Employee()
e1.set_name("Luca")
e1.del_name()
print(e1.get_name())


e2 = Employee()
e2.set_name("Kai")
print(e2.get_name())"""


#school programm
class School():
    def __init__(self,name,level,numberofstudents):
        self.name = name
        self.level = level
        self.numberofstudents = numberofstudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberofstudents(self):
        return self.numberofstudents

    def __repr__(self):
        return f"{self.name} is a {self.level} school with {self.numberofstudents} students"
a = School("Lboro","Uni",40000)
print(a.get_name())
print(a.get_level())
print(a.get_numberofstudents())
print(a)

class PrimarySchool(School):
    def __init__(self,name,numberofstudents,pickuppolicy):
        super().__init__(name,"Primary",numberofstudents)
        self.pickuppolicy = pickuppolicy

    def get_pickuppolicy(self):
        return self.pickuppolicy

    def __repr__(self):
        schoolrepr = super().__repr__()
        return schoolrepr + f" Pickup policy: {self.pickuppolicy}"

b = PrimarySchool("JP", 250, "after 3pm")
print(b.get_pickuppolicy())
print(b.get_level())
print(b)

class HighSchool(School):
    def __init__(self,name,numberofstudents,**sportsteams):
        super().__init__(name,"High",numberofstudents)
        self.sportsteams = sportsteams

    def get_sportsteams(self):
        return self.sportsteams

    def __repr__(self):
        return f"The availble sports teams are {self.sportsteams}"
c = HighSchool("LFCG", 1000, Football= "A team, B Team", Tennis = "Div 1, Div 2" )
print(c.get_sportsteams())
print(c.get_name())
print(c)












































