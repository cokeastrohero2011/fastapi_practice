from sqlmodel import SQLModel, create_engine, Session

connection ="postgresql://myuser:12345@localhost:5432/mydatabase"

engine = create_engine(connection)

print(engine)

def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)