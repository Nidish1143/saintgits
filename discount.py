discount=int(input("purchase quantity :"))
cost=int(input("enter cost:"))
if(cost>1000):
    print("after dicount rate",discount+(discount)*10/100)
else:
    print("no discount rate")
