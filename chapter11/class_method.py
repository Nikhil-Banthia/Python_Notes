#@classmethod decorator is used to create a class method 
#a classmethod is a method which is bound to a class not to a object

class employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"the class value of a is {cls.a}")

e = employee()
e.a = 45

e.show()
