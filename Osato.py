class Book:
    def __init__(self, title, author, isbn, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, isbn, publication_date):
        book = Book(title, author, isbn, publication_date)
        self.books.append(book)
        print(f"Book '{title}' added to {self.name}.")

    def display_books(self):
        if not self.books:
            print(f"{self.name} is empty.")
        else:
            print(f"Books in {self.name}:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Publication Date: {book.publication_date}")

    # ... rest of the methods ...

def main():
    library = Library("John Harris Library")

    while True:
        print("\nLibrary Management System -", library.name)
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            publication_date = input("Enter the publication date of the book: ")
            library.add_book(title, author, isbn, publication_date)
        elif choice == "2":
            library.display_books()
        # ... implement the other menu options ...
        elif choice == "5":
            print(f"Thank you for using {library.name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
