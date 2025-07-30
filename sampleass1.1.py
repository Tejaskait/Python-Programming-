import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
d = input("Enter operator (+, -, *, /): ")

if(d=="+"):
    e=a+b
    print("addition is \n",e)
elif(d=="-"):
    e=a-b
    print("subtraction is \n",e)
elif(d=="/"):
    e=a/b
    print("division is",e)
elif(d=="*"):
    e=a*b
    print("multiplication is",e)
elif(d=="log10"):
    e=math.log10(a)
    print("log of a is",a)
elif(d=="sin"):
    e=math.sin(a)
    print("sin of a",a)
elif(d=="cos"):
    e=math.cos(a)
    print("cos of a is",a)

