# Magic Methods - Dunder methods (double underscore) __init__, __str__, __repr__, etc
#                 They are autmatically called by many of python's built-in operations
#                 They allow us to define or customize the behavior of objects



class Book:
# Constructor method to initialize the object
    def __init__(self,title, author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
# String representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# comparison method to compare two Book objects
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author

# Less than method to compare two Book objects based on pages
    def __lt__(self, value):
        return self.pages < value.pages
    
# Greater than method to compare two Book objects based on pages
    def __gt__(self, value):
        return self.pages > value.pages
    
# Add method to add the number of pages of two Book objects    
    def __add__(self, value):
        return f"{self.pages + value.pages} pages in total"

# Check if a keyword is in the title or author of the book
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

# 
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author

book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Art of War", "Sun Tzu", 150)
book3 = Book("Berserk", "Kentaro Miura", 1000)
book4 = Book("Python 101", "John Doe", 220)


print(book1)
print(book1 == book4) # True, same title and author
print(book1 < book3)  # True, 300 < 1000
print(book1 > book2)  # True, 300 > 150
print(book1 + book3) # "1300 pages in total"
print("Python" in book1)  # True, "Python" is in the title
print(book3["title"])
print(book3["author"])