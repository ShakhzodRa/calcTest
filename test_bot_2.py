import os
import asyncio
from dotenv import load_dotenv

from database.db import SessionLocal, Users


import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, User, Chat
from aiogram.methods import GetChatMember
from sqlalchemy.orm import Session



load_dotenv()
token = "7561606009:AAEb5_ZvepQ_cIybdStrX4IHgeD9xGIKX-s"
print(token)
dp = Dispatcher()




def get_db(): # функция открытия шлюза подключения
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_person(username: str, db):
    person = db.query(Users).filter(Users.username == username).first() # проверь квери параметр в таблице Users, по фильтру Users.username. Оно должно значить username(который мы передали). Дай первый результат
    if person is None: # если такого юзера нет, то верни None
        return None
    return person # а если юзер есть, верни юзера

def add_new_person(username: str, db):
    new_user = Users(username=username) # передали в таблицу переменную username
    db.add(new_user) # добавили изменения в таблицу
    db.commit() # закрепили изменения
    db.refresh(new_user) # обновили
    return new_user # вернули new_user




@dp.message(Command("start"))
async def start(message: Message) -> None:
    username = message.from_user.username
    db = next(get_db()) # открываем шлюз в БД
    person = check_person(username, db)
    if not person:
        person = add_new_person(username, db)
        await message.answer(f"Привет {username} ты новенький")
        return
    await message.answer(f"Привет {username}, я тебя уже знаю!")





# @dp.message(Command("start"))
# async def start(message: Message) -> None:
#     username=message.from_user.username
#     db = next(get_db())
#     person = check_person(username, db)
#     if not person:
#         person = create_person(username, db)
#         await message.answer(f"Привет {username}, вижу, ты ещё не создавал записей")
#         return
#     await message.answer(f"Привет {username}, что добавишь сегодня?")
#     db.close()



async def main() -> None:
    bot = Bot(token=token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())