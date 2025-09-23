# f= open("Hello.txt" , "r")
# content= f.read()

# print(content)

# exec(content)

# f.close()


f= open("Hello.txt" , "r")
content= f.read()

f= open("code.py" , "w")
f.write(content)

f.close()

import code


