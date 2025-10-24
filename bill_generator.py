print("number of items purchased")
items_quantity=int(input())
total=0
for i in range(1,items_quantity+1):
    print("cost of item number",i)
    cost=float(input())
    total+=cost
total_bill=total
print("your toatal bill is ",total_bill)
if total_bill>100:
    print("congrats you got 10% off on your bill amount")
    print("your bill is ",0.9*total_bill)
else:
    print("your toatal bill is ",total_bill)
    



