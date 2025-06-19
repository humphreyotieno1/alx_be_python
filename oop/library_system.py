# Inheritance and Composition
class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)
    
    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}KB"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)
    
    def __str__(self):
        return f"{super().__str__()}, Page Count: {self.page_count}"
