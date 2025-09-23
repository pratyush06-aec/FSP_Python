t= int(input())
for i in range(t):
    m= int(input())
    n= int(input())
    c= [int(a) for a in input().split()]
    b= False
    for i in range(n):
        for j in range(i+ 1, n):
            if c[i]+c[j]== m:
                print(i+ 1, j+ 1)
                b= True
                break
        if b:
            break