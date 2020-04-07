from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def get_all_books():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()] # returns list of tuples
    return books


def insert_book(name, author):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def mark_book_as_read(name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))



