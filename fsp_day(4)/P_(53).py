try:
    f= open("File_1.txt" , "r")
    f.read()

    print(f)

    f.close()

except FileNotFoundError as f:
    print(f)