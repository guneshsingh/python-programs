a=float(input("Enter First no.:"))
b=float(input("Enter Second no.:"))
c=input("Enter the operation to be performed(+,-,*,/,%):")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
elif(c=="%"):
    print(a%b)
else:
    print("Invalid input")
