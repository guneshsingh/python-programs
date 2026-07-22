a=float(input("Enter First no.:"))
b=float(input("Enter Second no.:"))
c=input("Enter the operation to be performed(+,-,*,/,%):")
if(c=="+"):
    print(f"The sum of {a} and {b} is:",a+b)
elif(c=="-"):
    print(f"The difference of {a} and {b} is:",a-b)
elif(c=="*"):
    print(f"The multiplication of {a} and {b} is:",a*b)
elif(c=="/"):
    print(f"The sum of {a} and {b} is:",a/b)
elif(c=="%"):
    print(f"The sum of {a} and {b} is:",a%b)
else:
    print("Invalid input")
