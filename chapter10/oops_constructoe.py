class employee:
    name = "nikhil"
    language = "py"
    salary = 1200000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("constructor called")

    def getInfo(self):
        print(f"the language is {self.language}. The salary is{self.salary}")

    @staticmethod
    def greet():
        print("the language ")

harry = employee("harry",130000,"java")#class atri
print(harry.name,harry.salary)



 