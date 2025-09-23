def fibonacci(n):
    if(n== 0 or n==1):
        return n
    else:
        return fibonacci(n- 1)+ fibonacci(n- 2)
    
a= int(input("Enter the number: "))
for i in range(a):
    # print(f"The fibonacci series of {i} is {fibonacci(i)}")
    print(fibonacci(i), end=" ")


    