class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        found = False
        for book in books:
            if title in book:
                found = True
                continue
            updated_books.append(book)
        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found.")

# Creating Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q' :
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
