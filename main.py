import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message

from config import config  # Config
import AI
API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!Я шар,задавай вопрос и я отвечу на него")  # Отвечаем на полученное сообщение


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
@dp.message(Command(commands='help'))
async def handle_help(message: Message):
    await message.answer('Типа помощь')
@dp.message(F.text)
async def do_answer(message: Message):
    answer = AI.generate_answer()
    if answer:
        await message.answer(answer)
@dp.message(F.photo)
async def write(message: Message):
    await message.answer('Я не понимаю вас')
@dp.message(F.sticker)
async def write(message: Message):
    await message.answer('Я не понимаю вас')
@dp.message(F.voice)
async def write(message: Message):
    await message.answer('Я не понимаю вас')


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')