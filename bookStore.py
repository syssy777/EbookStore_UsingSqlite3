import eBookStore_Database

menu_prompt = """--------- MENU ------------
Please chose one of these options
1) To Add a New Book.
2) To Update Book.
3) To Delete Book.
4) To Search for Books.
0) To Exit.\n
Type your selection here:"""


def menu():
    my_db = eBookStore_Database.connect_DB()
    eBookStore_Database.create_table(my_db)

    while (user_input := input(menu_prompt)) != "5":
        print(user_input)
        if user_input == '0':
            my_db.close()
            exit()
        elif user_input == '1':
            prompt_addNew_book(my_db)
            my_db.commit()

        elif user_input == '2':
            prompt_Update_book(my_db)
            my_db.commit()

        elif user_input == '3':
            prompt_Delete_book(my_db)
            my_db.commit()

        elif user_input == '4':
            option = input(" Enter T to search by Title/Author\n Enter A to view entire Bookstore: ").upper()
            if option == 'A':
                prompt_seeAll_books(my_db)
            else:
                prompt_see_by_title_author(my_db)

        else:
            print('Invalid Input, Try Again !!!')


def prompt_addNew_book(my_db):
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    qty = int(input("Enter Quantity: "))
    eBookStore_Database.enter_book(my_db, title, author, qty)
    my_db.commit()


def prompt_Update_book(my_db):
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    qty = input("Enter Quantity: ")
    id = input("Enter Book ID: ")
    eBookStore_Database.update_a_book(my_db, title, author, qty, id)
    my_db.commit()


def prompt_Delete_book(my_db):
    id = input("Enter Book ID: ")
    eBookStore_Database.delete_a_book(my_db, id)
    my_db.commit()


def prompt_seeAll_books(my_db):
    books = eBookStore_Database.search_All(my_db)
    for book in books:
        print(f'{book[0]} - {book[1]} - ({book[2]}) - {book[3]}')
        my_db.commit()


def prompt_see_by_title_author(my_db):
    search = input("Search Book By Title/ Author: ")
    get = eBookStore_Database.search_one_book(my_db, search, search)
    for book in get:
        print(f'{book[0]} - {book[1]} - ({book[2]}) - {book[3]}')
        my_db.commit()


menu()
