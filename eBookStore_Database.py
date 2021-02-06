import sqlite3

books_table = "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,Title TEXT, Author TEXT, Qty INTEGER )"
insert_NewBook = "INSERT INTO books(Title, Author, Qty ) VALUES(?,?,?)"
update_Book = "UPDATE books SET Title= ?, Author= ?, Qty= ? WHERE id =?"
delete_book = "DELETE FROM books WHERE id = ?"
search_a_book = "SELECT * FROM books WHERE Author LIKE ? OR Title LIKE ? "
search_all_books = "SELECT * FROM books"


def connect_DB():
    return sqlite3.connect('ebookstore.db')


def create_table(my_db):
    with my_db:
        my_db.execute(books_table)


def enter_book(my_db, Title, Author, Qty):
    with my_db:
        my_db.execute(insert_NewBook, (Title, Author, Qty))


def update_a_book(my_db, Title, Author, Qty, id):
    with my_db:
        my_db.execute(update_Book, (Title, Author, Qty, id))


def delete_a_book(my_db, id):
    with my_db:
        my_db.execute(delete_book, (id,))


def search_one_book(my_db,Title, Author):
    with my_db:
        return my_db.execute(search_a_book, (Title, Author)).fetchall()


def search_All(my_db):
    with my_db:
        return my_db.execute(search_all_books).fetchall()

