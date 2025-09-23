a= int(input("Enter the range: "))
print(f"The range you have set is {a}")

factorial= 1

for i in range(1, a+ 1):
    factorial*= i
print(f"The factorial of {a} is {factorial}")
