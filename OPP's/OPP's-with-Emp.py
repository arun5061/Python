import email
class Employee:
    def __init__(self, first, last):
        self.first=first
        self.last=last
        #self.email='{}.{}@email.com'.format(self.first,self.last)
    '''Getter Decorato'''
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    '''Setter Decorator'''
    @fullname.setter
    def fullname(self, name):
        first, last =name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('You are at deleter')
        self.first=None
        self.last=None

class Develper(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last)
        self.pay=pay
    def __repr__(self):
        return "Developer({}, {}, {})".format(self.first, self.last, self.pay)
    @classmethod
    def form_str(cls,name):
        first, last, pay = name.split(' ')
        return(Develper(first, last, pay))

Dev_1="Tharun kumar 12000"
new_dev1=Develper.form_str(Dev_1)
print(new_dev1.fullname)
print(new_dev1.email)
emp_1=Develper('Arun','Kumar', 3000)
print(emp_1.fullname)
emp_1.fullname= 'Mohan Krishna'
print(emp_1.fullname)
print(emp_1.email)
print(repr(emp_1))
del emp_1.fullname
print(emp_1.fullname)
''' Will try now Setter, Getter, Deleter - Decorators'''
