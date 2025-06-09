import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column, Integer, String, Date, Float
from datetime import date



engine = create_engine("postgresql://myuser:mypassword@localhost:5433/mydatabase")


class Base(DeclarativeBase):
    pass


class Users(Base): # Таблица наследуется от Base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # Даём Типизацию (int, str и тд.), даём ключ связи
    username = Column(String)

class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=date.today)
    amount = Column(Float)




SessionLocal = sessionmaker(autoflush=False, bind=engine) # создание сессии переменной

Base.metadata.create_all(bind=engine) # передача метадаты