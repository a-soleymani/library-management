import library

lib = library.Library()

while True:
    print("1. add book")
    print("2. show books")
    print("3. remove book")
    print("4. search book")
    print("5. exit")


    choice = input("Make choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        lib.add_book(title, author)

    elif choice == "2":
        lib.show_books()


    elif choice == "3":
        title = input("Enter book title: ")
        lib.remove_book(title)
        print('Book has been removed')
    elif choice == "4":
        title = input("Enter book title: ")
        lib.search_book(title)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
