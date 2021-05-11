from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///library.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Withdrawal(Base):
    __tablename__ = 'withdrawals'
    id = Column(Integer, primary_key=True)
    book_barcode = Column(String, ForeignKey('books.barcode'))
    book = relationship('Book')
    student_name = Column(String)
    student_grade = Column(String)
    withdrawal_date = Column(String)
    return_date = Column(String)


class Book(Base):
    __tablename__ = 'books'
    barcode = Column(String, primary_key=True, unique=True)
    title = Column(String)
    author = Column(String)
    amount_available = Column(Integer)
    amount_borrowed = Column(Integer)


Base.metadata.create_all(engine)
