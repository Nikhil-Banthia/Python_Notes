f = open("poen.txt")
content = f.read()
if("nikhil" in content):
    print("word is present")
else:
    print("not present")
f.close()