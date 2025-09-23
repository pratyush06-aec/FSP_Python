a= "12345"
for i in range(5):
    print((" ")*(5-i)+ (a[i::-1])+(" ")*(i-5)+ (a[1:i]))