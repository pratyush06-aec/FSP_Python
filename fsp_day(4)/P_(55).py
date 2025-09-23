try:
    for i in range(2):
        a= int(input("Enter the number: "))
        print(a)

except ValueError as v:
    print("Hiii, values other than numbers or digits are not allowed!!!!")
