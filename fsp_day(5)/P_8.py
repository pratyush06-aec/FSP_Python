class Animal:
    def info(self):
        print("This is an animal!!!")

class Pet:
    def info(self):
        print("This is a pet!!!")

class Dog(Animal, Pet):
    def info(self):
        print("This is a dog!!!")

o= Dog()
o.info()


