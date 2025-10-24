import random,sys
print('guess a number')
n=random.randint(1,100)
while True:
    def guess(n):
        x=int(input())
        if x==n:
            return "you are correct"
            sys.exit()
        elif x<n:
            return "try with greater number"
        else:
            return "try with lesser number"
    print(guess(n))
