a= int(input("Enter the value for a: "))
b= int(input("Enter the value for b: "))
c= int(input("Enter the value for c: "))

if(a>b and a>c):
    print("a is greatest")
elif(b>c and b>a):
    print("b is greatest")
else:
    print("c is greatest")