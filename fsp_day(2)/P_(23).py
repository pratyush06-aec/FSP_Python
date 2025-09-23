a= []
n= int(input("Enter the number of values you want to enter: "))

for i in range(n):
    b= int(input("Enter the values: "))
    a.append(b)

a= list(set(a))

print(a)
