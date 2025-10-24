input()

print("welcome to the site,you can plan your daily tasks in here ")
print("")
name=input("please enter your name   ")
print("okay!",name,)

list=[]
task=input("what task do you like to perform?    ")
list.append(task)
print("")

print("now this is your todays to do list",   list)
print("")
print("")
print("do you want to make any changes")
print("")

changes=input("if yes press Y,if no press N  ")
if (changes=="Y"or"y"):
        while True:
            print("what changes do you like to make")
            print("")
            print("do you want to add more task to list?")
            print("")
            add=input("if yes prss Y if no press N  ")
            print("")
            if (add=="Y"or"y"):
                task1_0=input("next task you have to perform  ")
                list.append(task1_0)
                print("")
                print("your list is ")
                print(list)
            else:
                    print("ok then do you like to remove any task?")
                    print("")
                    remove=input("type Y for yes and N for no")
                    if (remove=="Y"or"y"):
                        print ("enter the task number you have to remove")
                        print("")

                        a=int(input())
                        if (a<=len(list)):
                            list.pop(a-1)
                            print("your to do list is")
                            print(list)
                        else:
                            print("you dont have that task number")
                    else:
                        print("sorry buddy thats all you can do here")
                        print("your final to do list is ",list)
else:
    print(list)
    print("you have",len(list),"tasks to do")
    print("be enthuisiastic and complete the task")
