n= int(input("Enter the number of students in class: "))
print(n)

marks= []

for i in range(n):
    score= int(input(f"Enter the score of {i+ 1}: "))
    print(score)
    marks.append(int(score))

print(marks)

for i in marks:
    if (i<38):
        print(i)

    elif((i%5)>2):
        print((i//5+1)*5)

    else:
        print(i)



