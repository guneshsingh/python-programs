# wap to chech wheter the number is odddd or evern
a=int(input("Enter the num :"))
if(a%2==0):{
    print("Even")
}
else:
    print("Odd")

    # wap to get the marks of 5 sybjkects of a student and casl the avg marks scored and cal grade obtained


s1=int(input("Enter first marks: "))
s2=int(input("Enter second marks: "))
s3=int(input("Enter third marks: "))
s4=int(input("Enter fourth marks: "))
s5=int(input("Enter fifth marks: "))
avg=(s1+s2+s3+s4+s5)/5.0
if(avg>90 and avg<101):
    print("A")
elif(avg>80 and avg<91):
    print("B")
elif(avg>70 and avg<81):
    print("C")
elif(avg>60 and avg<71):
    print("D")
elif(avg>50 and avg<61):
    print("E")
else:
    print("F")