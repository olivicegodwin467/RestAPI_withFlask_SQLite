from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)

def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(f"This is error\n {e}")
    
    return conn

@app.route("/books", methods=["GET", "POST"])
def books():
    conn = db_connect()
    cursor = conn.cursor()
    if request.method == "GET":
        querie = cursor.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in querie.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == "POST":
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        sql = """INSERT INTO book(author, language, title) VALUES (?, ?, ?)"""

        quer = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()

        return f"The book with ID: {quer.lastrowid} created successfully!!!", 201

@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    conn = db_connect()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
            if book is not None:
                return jsonify(book), 200
            else:
                return "Something went wrong!!", 404
            
    if request.method == "PUT":
        sql = """
UPDATE book SET author=?, language=?, title=? WHERE id=?
"""
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']

        new_book = {
            "id": id,
            "author": book['author'],
            "language": book['language'],
            "title": book['title']
        }
        cursor.execute(sql, (author, language, title, id))
        conn.commit()

        return jsonify(new_book)
    
    if request.method == "DELETE":
        sql = "DELETE FROM book WHERE id=?"
        cursor.execute(sql, (id,))
        conn.commit()
        return f"The book with ID: {id} has been deleted.", 200


if __name__ == "__main__":
    app.run(debug=True)