print("check year is leap year or not")
y=int(input("enter year:"))
if(y%4==0):
    if(y%100==0):
     if(y%400==0):
      print(y,"is leap year")
     else:
      print("not leap year")
    else:
      print("leap year")       
else:
    print("not a leap year")
