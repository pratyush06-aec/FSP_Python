class abc:
    a= 123

    def __init__(self, a, b):
        self.a= a
        self.b= b
        
    def ant(self):
        print(self.a + self.b)

o= abc(10, 20)
o.ant()
x= abc(20, 30)
x.ant()