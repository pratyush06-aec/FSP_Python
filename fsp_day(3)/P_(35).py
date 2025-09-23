list_1= ['a' , 'b' , 'c']
list_2= ['1' , '2' , '3']

list_3= [list_1[i]+list_2[i] for i in range(min(len(list_1) , len(list_2)))]
print(list_3)