class Manager:
    a=1

class employee(Manager):
    b=2

class programme(employee):
    c=3

o = employee()
print(o.a)
print(o.b)
print(o.c)#shows error because ther is no c atribute in employee
a = programme()
print(a.a)
print(a.b)
print(a.c)