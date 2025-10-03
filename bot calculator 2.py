x=float(input("enter the first number "))
y=float(input("enter the second number "))
operation=input("enter the operation you like to perform ")
if (operation=="+"):
    print("sum of two numbers", x+y )
elif(operation=="-"):
    if (x>=y):
        print("differnce of two numbers is ",x-y)
    else:
        print("difference of two numbers ",y-x)
elif(operation=="*"):
    print("product of two numbers is",x*y)
elif(operation=="/"):
    if(y!=0):
        print("quotient of 2 numbers is ",x/y)
        print("remainder=",x%y)
    else:
        print("cannot divide by 0")
else:
    print("invalid operation")
