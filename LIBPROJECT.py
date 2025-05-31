import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="", database="bookstore")
C = con.cursor()

def AddBook():
    book = input("Enter book name: ")
    genre = input("Enter genre: ")
    quantity = int(input("Enter quantity: "))
    author = input("Enter author: ")
    publication = input("Enter publication: ")
    price = float(input("Enter price: "))
    C.execute("INSERT INTO available_books VALUES (%s, %s, %s, %s, %s, %s)", (book, genre, quantity, author, publication, price))
    con.commit()
    print("Book added successfully!\n")

def DeleteBook():
    book = input("Enter book name to delete: ")
    C.execute("DELETE FROM available_books WHERE bookname = %s", (book,))
    con.commit()
    print("Book deleted successfully!\n")

def StaffDetailfS():
    staffname = input("Enter staff name: ")
    staffid = input("Enter staff ID: ")
    C.execute("INSERT INTO staff VALUES (%s, %s)", (staffname, staffid))
    con.commit()
    print("Staff added successfully!\n")

def StaffDetailfU():
    C.execute("SELECT * FROM staff")
    data = C.fetchall()
    print("\n--- Staff Details ---")
    for i in data:
        print("Name:", i[0], "| ID:", i[1])
    print()

def BookBuy():
    book = input("Enter the book name to buy: ")
    qty = int(input("Enter quantity: "))
    C.execute("SELECT quantity, price FROM available_books WHERE bookname = %s", (book,))
    data = C.fetchone()
    if data:
        available_qty, price = data
        if available_qty >= qty:
            total = qty * price
            C.execute("UPDATE available_books SET quantity = quantity - %s WHERE bookname = %s", (qty, book))
            C.execute("INSERT INTO sellrecord VALUES (%s, %s)", (book, total))
            con.commit()
            print(f"Purchased successfully! Total price: Rs.{total}\n")
        else:
            print("Not enough stock available.\n")
    else:
        print("Book not found.\n")

def SellRecord():
    C.execute("SELECT * FROM sellrecord")
    data = C.fetchall()
    print("\n--- Sell Records ---")
    for i in data:
        print("Book:", i[0], "| Amount:", i[1])
    print()

def TotalIncome():
    C.execute("SELECT SUM(price) FROM sellrecord")
    income = C.fetchone()[0]
    print(f"\nTotal Income: Rs.{income}\n")

def UsingBook():
    book = input("Enter book name to search: ")
    C.execute("SELECT * FROM available_books WHERE bookname = %s", (book,))
    data = C.fetchone()
    if data:
        print("\nBook Found:", data)
    else:
        print("Book not found.\n")

def UsingGenre():
    genre = input("Enter genre to search: ")
    C.execute("SELECT * FROM available_books WHERE genre = %s", (genre,))
    data = C.fetchall()
    if data:
        print("\n--- Books in Genre ---")
        for i in data:
            print(i)
    else:
        print("No books found in this genre.\n")

def UsingAuthor():
    author = input("Enter author name to search: ")
    C.execute("SELECT * FROM available_books WHERE author = %s", (author,))
    data = C.fetchall()
    if data:
        print("\n--- Books by Author ---")
        for i in data:
            print(i)
    else:
        print("No books found by this author.\n")

def Admin():
    while True:
        print("\n1. Add Book\n2. Delete Book\n3. Add Staff\n4. View Staff\n5. View Sell Record\n6. View Total Income\n7. Logout")
        n = int(input("Enter your choice: "))
        if n == 1:
            AddBook()
        elif n == 2:
            DeleteBook()
        elif n == 3:
            StaffDetailfS()
        elif n == 4:
            StaffDetailfU()
        elif n == 5:
            SellRecord()
        elif n == 6:
            TotalIncome()
        elif n == 7:
            break
        else:
            print("Invalid option. Try again.\n")

def Buyer():
    while True:
        print("\n1. Buy Book\n2. Search by Name\n3. Search by Genre\n4. Search by Author\n5. Logout")
        n = int(input("Enter your choice: "))
        if n == 1:
            BookBuy()
        elif n == 2:
            UsingBook()
        elif n == 3:
            UsingGenre()
        elif n == 4:
            UsingAuthor()
        elif n == 5:
            break
        else:
            print("Invalid option. Try again.\n")

def Main():
    while True:
        print("\n1. Admin Login\n2. Buyer Login\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user = input("Enter admin username: ")
            passwd = input("Enter admin password: ")
            C.execute("SELECT * FROM signup WHERE username = %s AND password = %s", (user, passwd))
            if C.fetchone():
                print("\nLogin successful.\n")
                Admin()
            else:
                print("Invalid credentials.\n")
        elif choice == 2:
            Buyer()
        elif choice == 3:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

Main()
