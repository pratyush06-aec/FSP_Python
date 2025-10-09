class library_contents:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)

class books(library_contents):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display_info(self):
        print("Book Info:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Pages:", self.pages)

class magazine(library_contents):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        print("Magazine Info:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Issue Number:", self.issue_number)

b = books("The Hobbit", "J.R.R. Tolkien", 1937, 310)
m = magazine("Time", "John Doe", 2025, 2307)

b.display_info()
print()
m.display_info()
