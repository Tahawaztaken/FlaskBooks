import sqlite3

connection = sqlite3.connect('books.sqlite')


cursor = connection.cursor()

sql_query = """ create table book (
    id integer primary key,
    author text not null,
    language text not null,
    title text not null
)"""

cursor.execute(sql_query)