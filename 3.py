# wap to find biggest of given 2 number from, the cmd prompt
a=int(input("Enter no:"))
b=int(input("Enter no:"))
if(a>b):
    print(f"{a} is greater")
else:
    print(f"{b} is greater")
# wap to find biggest of given 3 number from, the cmd prompt
a=int(input("Enter no:"))
b=int(input("Enter no:"))
c=int(input("Enter no:"))
if(a>b and a>c):
    print(f"{a} is greater")

elif(b>c):
        print(f"{b} is greater")
elif(c>b):
        print(f"{c} is gretaest")
else:
      print("all equal")