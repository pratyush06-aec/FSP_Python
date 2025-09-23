a= "123456789"
for i in range(0, 8):
    print(" "*(5-i)+(a[:i:])*(2*i-1))