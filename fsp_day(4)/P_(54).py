try:
    l= []
    for i in range(5):
        a= int(input(f"Enter the number at {i+ 1}: "))
        print(a)
        l.append(a)

    print(l)
    if(l[i]== True):
        print(a)

except IndexError as i:
    print(i)

