from sqlmodel import Session, SQLModel, create_engine

host = "db:3308"
db_name = "sample_db"
user = "mysqluser"
password = "mysqlpass"

DATABASE = f"mysql://{user}:{password}@{host}/{db_name}?charset=utf8"

engine = create_engine(DATABASE, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
