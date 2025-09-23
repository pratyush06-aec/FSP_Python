# a= []
# n= int(input("Enter the number of values you want: "))

# for i in range(n):
#     b= str(input("Enter the number: "))
#     a.append(b)

# print(a)

# x= int(input("Enter the length, in whose accordance you want the words to be printed: "))

# for i in range(n):
#     if(len(a[i])> x):
#         print(a[i])



a= []
n= int(input("Enter the number of words you want inside the list: "))

for i in range(n):
    b= str(input("Enter the names: "))
    a.append(b)

print(a)

for i in a:
    c= 0
    for x in i:
        c+= 1
    if(c> 3):
        print(i)







# Counter-controlled loop:
# A loop that runs a specific number of times, controlled by a counter variable. Example: for i in range(n): runs exactly



# Sentinel loop:
# A loop that continues until a special value (sentinel) is encountered. The sentinel value signals the end of input or processing. Example: reading values until the user enters -1




