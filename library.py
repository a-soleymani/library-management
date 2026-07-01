class Library:

    def __init__(self):
        self.library_books = []

    def add_book(self,title, author):
        self.library_books.append({
            "title": title,
            "author": author
        })


    def remove_book(self, title):
        for book in self.library_books:
            if book["title"] == title:
                self.library_books.remove(book)
                print("the book has been removed")
                return
        print('Book not found')
    def search_book(self, title):
        for book in self.library_books:
            if book["title"] == title:
                print(f"book {book['title']} by {book['author']} has been found")
                return
        print('book not found')

    def show_books(self):
        if not self.library_books:
            print("Library is empty")
            return
        for book in self.library_books:
            print(f"book {book['title']} by {book['author']}")

