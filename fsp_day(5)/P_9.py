class teacher:
    def info(self):
        print("Subject!!!")

class parent(teacher):
    def info_1(self):
        print("Occupation!!!")

class PersonInfo(parent):
    def info_2(self):
        print("This is the overall info!!!")

o= parent()
a= PersonInfo()

o.info()
o.info_1()
