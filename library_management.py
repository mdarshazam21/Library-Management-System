class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        print("-" * 40)
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("Status:", "Issued" if self.issued else "Available")


library = []


def load_data():
    try:
        with open("library.txt") as f:
            for line in f:
                line = line.strip()
                if not line:          
                    continue
                parts = line.split(",")
                if len(parts) != 4:  
                    continue
                bid, title, author, issued = parts
                b = Book(int(bid), title, author)
                b.issued = issued == "True"
                library.append(b)
    except FileNotFoundError:
        pass


def save_data():
    with open("library.txt", "w") as f:
        for b in library:
            f.write(f"{b.book_id},{b.title},{b.author},{b.issued}\n")


def find(bid):
    for b in library:
        if b.book_id == bid:
            return b
    return None


def add():
    try:
        bid = int(input("ID: ").strip())
        if find(bid):
            print("Duplicate ID")
            return
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        if not title or not author:
            print("Title and author cannot be empty.")
            return
        library.append(Book(bid, title, author))
        print("Book added successfully.")
    except ValueError:
        print("Invalid ID – please enter a number.")


def display():
    if not library:
        print("No books available.")
        return
    for book in library:
        book.display()


def search_id():
    try:
        bid = int(input("ID: ").strip())
        b = find(bid)
        if b:
            b.display()
        else:
            print("Not found")
    except ValueError:
        print("Invalid ID – please enter a number.")


def search_title():
    t = input("Title: ").strip().lower()
    if not t:
        print("Title cannot be empty.")
        return
    found = False
    for b in library:
        if b.title.lower() == t:
            b.display()
            found = True
    if not found:
        print("Not found")


def search_author():
    a = input("Author: ").strip().lower()
    if not a:
        print("Author cannot be empty.")
        return
    found = False
    for b in library:
        if b.author.lower() == a:
            b.display()
            found = True
    if not found:
        print("Not found")


def issue():
    try:
        bid = int(input("ID: ").strip())
    except ValueError:
        print("Invalid ID – please enter a number.")
        return
    b = find(bid)
    if not b:
        print("Not found")
    elif b.issued:
        print("Already issued")
    else:
        b.issued = True
        print("Issued")


def ret():
    try:
        bid = int(input("ID: ").strip())
    except ValueError:
        print("Invalid ID – please enter a number.")
        return
    b = find(bid)
    if not b:
        print("Not found")
    elif not b.issued:
        print("Already available")
    else:
        b.issued = False
        print("Returned")


def update():
    try:
        bid = int(input("ID: ").strip())
    except ValueError:
        print("Invalid ID – please enter a number.")
        return
    b = find(bid)
    if not b:
        print("Not found")
        return
    print("1. Title")
    print("2. Author")
    choice = input("Choice: ").strip()
    if choice == "1":
        new_title = input("New title: ").strip()
        if new_title:
            b.title = new_title
            print("Updated")
        else:
            print("Title cannot be empty.")
    elif choice == "2":
        new_author = input("New author: ").strip()
        if new_author:
            b.author = new_author
            print("Updated")
        else:
            print("Author cannot be empty.")
    else:
        print("Invalid choice")


def delete():
    try:
        bid = int(input("ID: ").strip())
    except ValueError:
        print("Invalid ID – please enter a number.")
        return
    b = find(bid)
    if b:
        confirm = input(f"Are you sure you want to delete '{b.title}'? (y/n): ").strip().lower()
        if confirm == 'y':
            library.remove(b)
            print("Deleted")
        else:
            print("Deletion cancelled.")
    else:
        print("Not found")


def count():
    total = len(library)
    issued = sum(1 for b in library if b.issued)
    print(f"Total Books     : {total}")
    print(f"Issued Books    : {issued}")
    print(f"Available Books : {total - issued}")


def sort_title():
    for b in sorted(library, key=lambda x: x.title.lower()):
        b.display()


def sort_author():
    for b in sorted(library, key=lambda x: x.author.lower()):
        b.display()


# Main program
load_data()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search by ID")
    print("4. Search by Title")
    print("5. Search by Author")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Update Book")
    print("9. Delete Book")
    print("10. Count Books")
    print("11. Sort by Title")
    print("12. Sort by Author")
    print("13. Save Data")
    print("14. Exit")

    choice = input("\nEnter Your Choice: ").strip()

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search_id()
    elif choice == "4":
        search_title()
    elif choice == "5":
        search_author()
    elif choice == "6":
        issue()
    elif choice == "7":
        ret()
    elif choice == "8":
        update()
    elif choice == "9":
        delete()
    elif choice == "10":
        count()
    elif choice == "11":
        sort_title()
    elif choice == "12":
        sort_author()
    elif choice == "13":
        save_data()
        print("Data saved.")
    elif choice == "14":
        save_data()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 14.")
