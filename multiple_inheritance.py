class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, e_name, e_salary, e_department, e_role):

        self.name = e_name
        self.salary = e_salary
        self.department = e_department
        self.role = e_role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}, Department is {self.department} and role is {self.role}"

    @classmethod
    def change_leave(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        #param = string.split("-")
        #return cls(param[0], param[1], param[2], param[3])
        return cls(*string.split("-"))


    @staticmethod
    def printgood(string):
        print("This is good " + string)



class Player:
    var = 10
    no_of_games = 4
    def __init__(self, g_name, g_game):
        self.name = g_name
        self.game = g_game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game} "


#class CoolProgramer(Employee, Player):
class CoolProgramer(Player, Employee):

    language = "Python"
    def printlanguage(self):
        print(self.language)



sabbir = Employee("Sabbir Ahamed", 1800, "IT", "Dev")
michael = Employee("Michael Horton", 2000, "IT", "Lead Dev")
Kelly = Employee.from_dash("Kelly Joyane-1300-IT-BA")


jack = Player("Jack Jonton", ["Football"])
#bidhan = CoolProgramer("Bidhan Prodhan", 2200, "IT", "Cool Programmer")
bidhan = CoolProgramer("Bidhan Prodhan", "Football")


#bidhan.printlanguage()

#det = bidhan.printdetails()

#print(det)

print(bidhan.var)



