books:list=[]
users:list=[]

books.append({"id":1,"title":"To kill a Mockingbird","author":"Harper Lee","genre":"fiction","status":"available"})
books.append({"id":2,"title":"1984","author":"george orwell","genre":"Dystopian","status":"checked out"})
books.append({"id":"3","title":"The great gatsby","author":"f.scott fitzgerald","genre":"classic","status":"available"})

users.append({"id":1,"name":"Alice","borrowed_books":[]})
users.append({"id":2,"name":"Bob","borrowed_books":[]})

def add_books(id:int, title:str, author:str, genre:str,status:str)->dict:
    book:dict = {"id":id, "title":title, "author":author, "genre":genre,"status":status}
    return book
def view_all_books():
    print("\nAll books:")
    for book in books:
        print(f"{book['id']}. \"{book['title']}\"by {book['author']}({book['status']})")
              
def search_books():
              
    search_type = input("search by (1) Title, (2) Author, (3) Genre: ")
    query = input("Enter search term: ").lower()
    print("\nsearch Results:")

    for book in books:
        if (search_type == "1" and query in book["title"].lower()) or \
           (search_type == "2" and query in book["author"].lower()) or \
           (search_type == "3" and query in book["genre"].lower()):
             print(f"{book['id']}. \"{book['title']}\"by {book['author']}({book['status']})")


def add_user(id:int, user_name:str, borrowed_books:list) -> dict:
    user:dict = {"id":id,"user_name":user_name,"borrowed_books":borrowed_books}
    return user


def view_checked_out_books() -> None:
    print("\nchecked out book:")
    for book in books:
        if book["status"=="Checked out"]:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']}")
            
def view_users():
    print("\nAll users:")
    for user in users:
        print(f"User ID: {user['id']}, Name: {user['name']}, Borrowed books: {', '.join(user['borrowed_books']) or 'None'}")
def borrow_book():
    user_id = int(input("Enter your User ID: "))
    book_id  = int(input("Enter the Book ID to borrow: "))

    user = next((user for user in users if user["id"]  == user_id), None)
    
    book = next((book for user in books if book["id"]  == book_id), None)
    if user and book:
        if book["status"] == "Available":
            book["status"] = "Checked out"
            user["borrowed_books"].append(book["title"])
            print(f"you have borrowed \"{book['title']}\".")
        else:
            print(f"Sorry, the book \ {book['title']}\" is currently checked out.")
    else:
        print("Invalid user ID or book ID.")

def return_book():
    user_id = int(input("Enter your user ID: "))
    book_id = int(input("Enter the book ID to return : "))

    user = next ((user for user in users if user["id"] ==user_id), None)
    book = next ((book for book in books if book["id"] ==book_id), None)     

    if user and book:
        if book["title"] in user["borrowed_books"]:
            book["status"] = "Available"
            user["borrowed_books"].remove(book["title"])
            print(f"you have returned \"{book['title']}\".")
        else:
            print("you haven't boorrowed this bookk.")
    else:
        print("Invalid user ID or book ID.")


def main_menu():
    while True:
        print("\nwelcome to the Community Library System!")
        print("----------------------------------------")
        print("1. view all books")
        print("2. search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. view all users")
        print("6. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            view_all_books()
        elif choice=="2":
            search_books()
        elif choice =="3":

            borrow_book()
        elif choice == "4":
             return_book()
        elif choice=="5":
              view_users()
        elif choice=="6":
            break
        else:
            print("Invalid choice. please enter a number 1 and 6.")

main_menu()            
    