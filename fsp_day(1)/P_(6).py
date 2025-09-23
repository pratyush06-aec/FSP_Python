electricity_bill= float(input("Enter your amount: "))
print(f"Your electricity bill is {electricity_bill} units")

# electricity_bill_1= ((electricity_bill*5)-100)
# electricity_bill_2= (electricity_bill*10)-((electricity_bill*5)-100)

if(electricity_bill>= 1 and electricity_bill<=100):
    print("You incurred zero amount of consumption!!!")

elif(electricity_bill>=101 and electricity_bill<=200):
    print((electricity_bill-100)*5)

else:
    print((electricity_bill-200)*10)