def num(*a):
    odd_count= 0
    even_count= 0
    for i in (a):
        if(i%2!= 0):
            odd_count+= 1

        else:
            even_count+= 1
    return odd_count, even_count


odd, even= num(2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"There are {even} even numbers and there are {odd} odd numbers")