from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel


app = FastAPI()

conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password ="12345",
    host="localhost",
    port=5432
)

print(conn)

cur = conn.cursor()

create_table_query = """
create table if not exists books(
book_id serial primary key,
book_name varchar,
book_author varchar)
"""

cur.execute(create_table_query)
conn.commit()


@app.get("/health_check")
def health_check():
    return "FastAPI is running properly"


class user_data(BaseModel):
    book_name : str
    book_author : str




@app.post("/add_books")
def add_books(data : user_data):
    insert_query = f"""
    insert into books(book_name,book_author)
    VALUES ('{data.book_name}','{data.book_author}')
"""
    
    cur.execute(insert_query)
    conn.commit()

    return "data added"


@app.get("/get_all_users")
def get_all_users():
    read_data_query = """
select * from books
"""
    cur.execute(read_data_query)
    rows = cur.fetchall()
    return(rows)



@app.get("/get_specific_users")
def get_specific_users(id: int):
    read_specific_user_query = f"""
select * from books where book_id = {id}
"""
    cur.execute(read_specific_user_query)
    rows = cur.fetchall()
    return rows




@app.delete("/delete_users/{id}")
def delete_users(id:int):
    delete_query = f"""
delete from books where book_id = {id}
"""
    cur.execute(delete_query)
    conn.commit()
    return "data deleted successfully"