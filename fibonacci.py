def fibonacci(n):
    global x
    x=input('enter the term of fibonacci series you want to:  ')
    if n<=0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(3))
    