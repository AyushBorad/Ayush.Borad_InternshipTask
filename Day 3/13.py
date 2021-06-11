n1=input("enter the first number:")
n2=input("enter the second number :")
n3=input("enter the third number :")

if n1>n2 and n2>n3:
    print("{} is the greatest number".format(n1))
elif n2>n1 and n1>n3:
    print("{} is the greatest number".format(n2))
else:
    print("{} is the greatest number".format(n3))
