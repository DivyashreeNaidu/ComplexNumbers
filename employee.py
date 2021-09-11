class Member:
    def __init__(self, name, age, phonenum, address, salary):
        self.name = name
        self.age = age
        self.phonenum = phonenum
        self.address = address
        self.salary = salary


o1 = Member("Divya", 21, 9998882223, "Ganapatipura Bangalore", 45000)
print("NAME: "+str(o1.salary))


class Employee(Member):
    def __init__(self, specialization, department):
        self.specialization = specialization
        self.department = department


class Manager(Member):
    def __init__(self, specialization, department):
        self.specialization = specialization
        self.department = department


e1 = Employee("python", "IT")
e1.__init__ = Member("divya", 21, 9966775588, "jp nagar bangalore", 90000)
m1 = Manager("Admin", "management")
m1.__init__ = Member("saras", 22, 9966775568, "RBI layout bangalore", 56000)
print('\nEmployee details\n' + 'Name: '+str(e1.__init__.name)+'\nAge: '+str(e1.__init__.age) +
      '\nPhone Number: ' + str(e1.__init__.phonenum)+'\nAddress: '+str(e1.__init__.address))
print('salary: ' + str(e1.__init__.salary) + '\nSpecialization: ' +
      e1.specialization + '\ndepartment: ' + e1.department)
print('\nManager details\n' + 'Name: '+str(m1.__init__.name)+'\nAge: '+str(m1.__init__.age) +
      '\nPhone Number: ' + str(m1.__init__.phonenum)+'\nAddress: '+str(m1.__init__.address))
print('salary: ' + str(m1.__init__.salary) + '\nSpecialization: ' +
      m1.specialization + '\ndepartment: ' + m1.department)
