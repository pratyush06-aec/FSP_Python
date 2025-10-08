## Inheritance:

    #    1. Single Inheritance
    #    2. Multiple Inheritance
    #    3. Multi-level Inheritance
    #    4. Hierarchical Inheritance
    #    5. Hybrid Inheritance



# class parent:                            # Example of (Single Inheritance).
#     def toy(self):
#         print("This is toy!!!")

# class child(parent):
#     def toy_2(self):
#         print("This is toy_2!!!")

# o= child()
# o.toy()
# o.toy_2()



# class parent_1:  
#     a= 12                             # Example of (Multi-level Inheritance).
#     def toy(self):
#         print("This is parent_1!!!")

# class parent_2(parent_1):
#     b= 34
#     def toy_2(self):
#         print("This is parent_2!!!!")

# class child(parent_2):
#     c= 34
#     def toy_3(self):
#         print("This is child here!!!!" , self.a, self.b, self.c)


# o= child()
# # o.toy()
# # o.toy_2()
# o.toy_3()




# class parent_1:
#     a= 34
#     def toy(self):
#         print("This is parent_1!!!")

# class parent_2:
#     b= 56
#     def toy_2(self):
#         print("This is parent_2!!!!")

# class child(parent_1, parent_2):          # Example of (Multiple Inheritance).
#     c= 78
#     def toy_3(self):
#         print("This is child here!!!!" , self.a, self.b, self.c)

# o= child()
# o.toy_3()



class parent:
    def toy(self):
        print("This is parent!!!")                  # Example of (Hierarchical Inheritance).

class child_1(parent):
    def toy_1(self):
        print("This is child_1!!!")

class child_2(parent):
    def toy_2(self):
        print("This is child_2!!!")

o= child_1()
x= child_2()

o.toy()
o.toy_1()
x.toy()
x.toy_2()








