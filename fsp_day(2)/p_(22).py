l= []
n= int(input("Enter the number of terms you want ot enter: "))

for i in range(n):
    a= int(input("Enter the value of a: "))
    l.append(a)

largest= l[0]

for num in l:
    if num>largest:
        largest= num

print(l)
print(largest)


