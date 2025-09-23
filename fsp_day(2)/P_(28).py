s= ()
l= list(s)

# print(type(s))

n= int(input("Enter the number: "))

for i in range(n):
    a= int(input("Enter the number: "))
    l.append(a)

s= tuple(l)
print(s)

print(max(s))
print(min(s))

sum= 0
for i in l:
    sum+= i

print(sum)
