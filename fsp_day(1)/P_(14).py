for i in range(1, 10):
    if(i<= 5):
        print((" ")*(5- i)+("*")*(2*i-1))
    else:
        print((" ")*abs(5- i)+ ("*")*(2*(10-i)-1))
