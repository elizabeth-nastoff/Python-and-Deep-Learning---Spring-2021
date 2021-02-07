class IterEmp(type):
    def __iter__(cls):
        return iter(cls._allEmp)

class Employee(metaclass=IterEmp):
    count = 0
    _allEmp = []

    def __init__(self, name, family, salary, department):
        self._allEmp.append(self)
        type(self).count += 1

        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    #def salaryAvg(self):
    #    total = 0
    #    for emp in Employee:
    #        total = total + emp.salary
    #    return round(total / Employee.count, 2)

class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

def salaryAvg():
    total = 0
    for emp in Employee:
        total = total + emp.salary
    return round(total/Employee.count, 2)


if __name__ == '__main__':
    Liz = Employee("Liz", 3, 70000, "IT")
    Alex = Employee("Alex", 4, 80000, "IT")
    Emylia = Employee("Emylia", 2, 50000, "HR")

    print (salaryAvg())


    Marley = FullTimeEmployee("Marley", 4, 90000, "IT")
    Mike = FullTimeEmployee("Mike", 2, 30000, "Sales")

    print (salaryAvg())
