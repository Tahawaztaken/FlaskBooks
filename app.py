from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    connection = None
    try:
        connection = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return connection

@app.route('/books', methods=['GET', 'POST'])
def books():
    connect_db = db_connection()
    cursor = connect_db.cursor()
    if request.method == 'GET':
        rows = cursor.execute("SELECT * FROM book").fetchall()
        return jsonify(rows)

    if request.method == 'POST':
        cursor.execute("INSERT INTO book VALUES(39, 'bob', 'english', 'bobs book')")
        connect_db.commit()


@app.route('/books/delete')
def delete():
    connect_db = db_connection()
    cursor = connect_db.cursor()
    iden = request.args.get('id')
    cursor.execute(f"DELETE FROM book WHERE id = {iden}")
    connect_db.commit()

if __name__ == '__main__':
    app.run(debug=True)