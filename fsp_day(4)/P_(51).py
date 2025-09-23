a= str(input("Enter any string: "))
print(a)
    
if(a.isnumeric()):
    raise ValueError("You enter numbers or digits, which is invalid here!!!!")
    
print(f"Hiii {a}!!!!")