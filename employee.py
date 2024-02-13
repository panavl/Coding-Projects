"""
  File: employee.py
  Description:

  Student Name: Wei-Yu Chiang
  Student UT EID: wc22968

  Partner Name: Panav Ladha
  Partner UT EID: pl22793

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 09-11-23
  Date Last Modified: 09-11-23
"""

class Employee:
    """Basic employee information."""
    def __init__(self, name, identifier, salary = None):
        self.name = name
        self.identifier = identifier
        self.salary = salary

    def __str__(self):
        return  f'Employee\n{self.name},{self.identifier},{self.salary}'


############################################################
############################################################
############################################################

class PermanentEmployee(Employee):
    """Employee with benefits."""
    def __init__(self, benefits, **kwargs):
        super().__init__(**kwargs)
        self.benefits = benefits

    def cal_salary(self):
        """Calculate the actual salary considering benefits."""
        actual_salary = self.salary
        if self.benefits == ['health_insurance']:
            actual_salary = self.salary *0.9
        elif self.benefits == ['retirement']:
            actual_salary = self.salary * 0.8
        elif self.benefits == ["retirement", "health_insurance"]:
            actual_salary = self.salary *0.7

        return actual_salary

    def __str__(self):
        return  f'PermanentEmployee\n{self.name},{self.identifier},{self.salary},{self.benefits}'



############################################################
############################################################
############################################################

class Manager(Employee):
    """Employee with a bonus."""
    def __init__(self, bonus,**kwargs):
        super().__init__(**kwargs)
        self.bonus = bonus

    def cal_salary(self):
        """Calculate the total salary including the bonus."""
        return self.salary + self.bonus

    def __str__(self):
        return  f'Manager\n{self.name},{self.identifier},{self.salary},{self.bonus}'




############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    """Temporary employee with hourly wage."""
    def __init__(self, hours, **kwargs):
        super().__init__(**kwargs)
        self.hours = hours

    def cal_salary(self):
        """Calculate the salary based on hourly wage and hours worked."""
        return self.salary * self.hours

    def __str__(self):
        return  f'TemporaryEmployee\n{self.name},{self.identifier},{self.salary},{self.hours}'


############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    """Temporary employee with travel expenses."""
    def __init__(self, travel, **kwargs):
        super().__init__(**kwargs)
        self.travel = travel

    def cal_salary(self):
        salary_hours = TemporaryEmployee.cal_salary(self)

        return salary_hours + (self.travel * 1000)

    def __str__(self):
        return f'Consultant\n{self.name},{self.identifier},{self.salary},{self.hours},{self.travel}'


############################################################
############################################################
############################################################


class ConsultantManager(Consultant,Manager):
    """Employee with both consulting and managerial roles."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cal_salary(self):
        con_sal = Consultant.cal_salary(self)
        man_sal = Manager.cal_salary(self)
        return con_sal + man_sal - self.salary

    def __str__(self):
        return f'ConsultantManager\n{self.name},{self.identifier},{self.salary},{self.hours},{self.travel}'



############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
    main()
