def myfunc():

        value = 42

        match value:
            case 0:
                print("Zero")
            case 1 | 2:
                print("One or Two")
            case 42:
                print("The Answer to the Ultimate Question of Life")
            case _:
                print("Something else")


if __name__ =="__main__": 
    print ("we are directly running thhis code")
    myfunc()