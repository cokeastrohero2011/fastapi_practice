from sqlmodel import SQLModel, Field, select
from connection import create_tables, get_session



class Users(SQLModel, table = True):
    id : int = Field(primary_key= True)
    user_name: str
    password: str

class employee(SQLModel, table = True):
    id : int = Field(primary_key= True)
    employee_name: str
    employee_email: str
    emplyee_phoneno: str


class books_copy (SQLModel, table = True):
    id : int = Field(primary_key= True)
    book_name: str
    book_author: str
    book_year: int
    sold : bool


create_tables()

# inserting data to books_copy

"""
with get_session() as db:
    insert_data = books_copy(book_name = "Camping 101", book_author= "Alex", book_year= 2021, sold = True)
    db.add(insert_data)
    db.commit()
print("DATA ADDED")
"""

# get all data
"""
with get_session() as db:
    read_data = db.exec(select (books_copy)).all()
    print(read_data)
"""

# get specific data
"""
with get_session() as db:
    read_specific_data = db.get(books_copy, 2)
    print(read_specific_data)
"""

# delete data
"""
with get_session() as db:
    delete_data = db.get(books_copy, 2)
    db.delete(delete_data)
    db.commit()
"""


#update data
with get_session() as db:
    update_data = db.get(books_copy, 3)
    update_data.book_author = "Sam Altman"
    update_data.book_year = 2010
    db.add(update_data)
    db.commit()