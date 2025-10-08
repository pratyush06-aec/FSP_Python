class string_manipulator:
    def __init__(self):
        self.user_string = ""

    def get_string(self):
        self.user_string = str(input("Enter a string: "))

    def print_string(self):
        print(self.user_string.upper())

#Example usage:
if __name__ == "__main__":
    sm = string_manipulator()
    sm.get_string()
    sm.print_string()


