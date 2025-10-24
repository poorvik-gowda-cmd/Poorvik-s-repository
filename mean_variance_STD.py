from math import*
print("number of elements:")
n=int(input())
list=[]
for i in range(n):
    list.append(float(input()))
  

#mean                       #mean
mean=sum(list)/n            #for ele in list:
print("mean = ",mean)       #mean=sum(ele)/n
                            #print(mean)          why isnt this 

#variance
for ele in list:
    meansquare=(ele - mean)**2/n
variance=(meansquare)
print("variance = ",variance)


#standard deviation
STD=sqrt(variance)
print("standard deviation = ",STD)