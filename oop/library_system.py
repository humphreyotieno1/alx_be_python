# Inheritance and Composition
class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)
        
# Composition
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            return True
        else:
            print("Error: Only Book objects can be added to the library")
            return False
            
    def list_books(self):
        if not self.books:
            print("The library is empty")
            return
        
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")
