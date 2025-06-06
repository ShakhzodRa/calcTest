import asyncio
import logging
import os 
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

load_dotenv()
token = os.getenv("BOT_TOKEN")
dp = Dispatcher()
rt = Router()
class CalcNumber(StatesGroup):
    firstNum = State()
    secondNum = State()
    operation = State()

@rt.message(Command("start"))
async def startCalc(message: Message, state: FSMContext) -> None:
    await message.answer("Привет! Я помогаю с простыми операциями, напиши мне первое число!")
    await state.set_state(CalcNumber.firstNum)

@rt.message(CalcNumber.firstNum)
async def enterFirstNum(message: Message, state: FSMContext) -> None:
    floatUpdate = message.text.replace(",", ".")
    try:
        number = float(floatUpdate)
    except ValueError:
        await message.answer("Введи число, не что-то другое")
        return

    await state.update_data(firstNum = number)
    await message.answer("Ура, получилось, введи второе число!")
    await state.set_state(CalcNumber.secondNum)

@rt.message(CalcNumber.secondNum)
async def enterSecondNum(message: Message, state: FSMContext) -> None:
    floatUpdate = message.text.replace(",", ".")
    try:
        number = float(floatUpdate)
    except ValueError:
        await message.answer("Введи число, не что-то другое")
        return
    await state.update_data(secondNum = number)
    await message.answer("Введи теперь операцию, которую хочешь провести с этими числами, например: сложение/вычетание/деление/умножение")
    await state.set_state(CalcNumber.operation)

@rt.message(CalcNumber.operation)
async def operationWithNums(message: Message, state: FSMContext) -> None:
    if message.text.lower() == "сложение":
        data = await state.get_data()
        firstNum = data.get("firstNum")
        secondNum = data.get("secondNum")

        result = firstNum + secondNum
        await message.answer(f"Вот результат операции {result}")

    elif message.text.lower() == "умножение":
        data = await state.get_data()
        firstNum = data.get("firstNum")
        secondNum = data.get("secondNum")

        result = firstNum * secondNum
        await message.answer(f"Вот результат операции {result}")

    elif message.text.lower() == "деление":
        data = await state.get_data()
        firstNum = data.get("firstNum")
        secondNum = data.get("secondNum")

        result = firstNum / secondNum
        await message.answer(f"Вот результат операции {result}")

    elif message.text.lower() == "вычетание":
        data = await state.get_data()
        firstNum = data.get("firstNum")
        secondNum = data.get("secondNum")

        result = firstNum - secondNum

    else:
        await message.answer("Введи операци корретно!")
        return

async def main() -> None:
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(rt)
    await dp.start_polling(bot)

# алина шлюха

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())