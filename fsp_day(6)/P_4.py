x1, v1, x2, v2= input().strip().split(" ")
x1, v1, x2, v2= [int(x1), int(v1), int(x2), int(v2)]
found= False
for i in range(10000):
    if x1+v1*i == x2+v2*i:
        print("Yes")
        found= True
        break
if not found:
    print("No")
