class employee:
    name = "nikhil"
    language = "py"
    salary = 1200000

    def getinfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}")

harry = employee()#class atri
print(harry.name,harry.salary)
harry.getinfo()

nikhil = employee()
nikhil.language = "java" #inst atri
print(nikhil.name,nikhil.language)
nikhil.getinfo()