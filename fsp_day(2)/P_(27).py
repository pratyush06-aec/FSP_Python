s= {1, 2, 3, 4, 5}

print(s)
# print(type(s))

a= int(input("Enter the number: "))

for i in s:
    if(i== a):
        print(i)

c= int(input("Enter the number: "))

s.add(c)
print(s)

d= int(input("Enter the number: "))

s.remove(d)
print(s)

