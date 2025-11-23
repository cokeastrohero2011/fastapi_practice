from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from pathlib import Path

app = FastAPI()

# -----------------------------
# 1. Connect to SQLite database
# -----------------------------
# This will create a file "books.db" in the current directory if it doesn't exist.
DB_PATH = Path("/home/ahmedansari/Documents/fastapi_practice/test.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

# -------------------------------------
# 2. Create table if it doesn't exist
# -------------------------------------
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    book_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name   TEXT,
    book_author TEXT
);
"""

cur.execute(create_table_query)
conn.commit()


# -----------------------------
# 3. Health check endpoint
# -----------------------------
@app.get("/health_check")
def health_check():
    return "FastAPI is running properly with SQLite"


# -----------------------------
# 4. Pydantic model
# -----------------------------
class UserData(BaseModel):
    book_name: str
    book_author: str


# -----------------------------
# 5. Add book (CREATE)
# -----------------------------
@app.post("/add_books")
def add_books(data: UserData):
    insert_query = """
    INSERT INTO books (book_name, book_author)
    VALUES (?, ?)
    """
    # Use parameterized queries to avoid SQL injection
    cur.execute(insert_query, (data.book_name, data.book_author))
    conn.commit()
    return "data added"


# -----------------------------
# 6. Get all books (READ)
# -----------------------------
@app.get("/get_all_users")
def get_all_users():
    read_data_query = """
    SELECT * FROM books
    """
    cur.execute(read_data_query)
    rows = cur.fetchall()

    # Convert rows (tuples) to a list of dicts for nicer JSON
    result = [
        {"book_id": r[0], "book_name": r[1], "book_author": r[2]}
        for r in rows
    ]
    return result


# -----------------------------
# 7. Get specific book by id (READ)
# -----------------------------
@app.get("/get_specific_users")
def get_specific_users(id: int):
    read_specific_user_query = """
    SELECT * FROM books WHERE book_id = ?
    """
    cur.execute(read_specific_user_query, (id,))
    rows = cur.fetchall()

    result = [
        {"book_id": r[0], "book_name": r[1], "book_author": r[2]}
        for r in rows
    ]
    return result


# -----------------------------
# 8. Delete book by id (DELETE)
# -----------------------------
@app.delete("/delete_users/{id}")
def delete_users(id: int):
    delete_query = """
    DELETE FROM books WHERE book_id = ?
    """
    cur.execute(delete_query, (id,))
    conn.commit()
    return "data deleted successfully"