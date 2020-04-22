import os,csv
from books import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv("DATABASE_URL"))
database = scoped_session(sessionmaker(bind=engine))
database.create_all()
Base = declarative_base()   

def main():
    Base.metadata.create_all(bind=engine)
    f = open("books.csv")
    book_details = csv.reader(f)
    next(book_details)
    for isbn,title,author,year in book_details:
        book = Books(title = title, author = author, isbn = isbn, year = year)
        database.add(book)
    database.commit()
    database.close()

if __name__ == "__main__":
    main()                              