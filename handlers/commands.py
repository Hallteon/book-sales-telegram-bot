from . import markups
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command

from utils import parsers
from loader import dp, bot


@dp.message_handler(Command("sales"))
async def book_sales(message: types.Message):
    await message.answer("Выберите книжный интернет-магазин, чтобы узнать об "
                         "актуальных скидках и акциях в нём 🎁", reply_markup=markups.menu)


@dp.message_handler(text="Book24 📙")
async def book24_sales(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)

    sales = await parsers.scraper_book24()

    sales_names = sales["sales"]
    descriptions = sales["descriptions"]
    before = sales["before"]
    links = sales["links"]

    text = "<b>Список акций в интернет-магазине book24 📚:</b>\n"

    for sale, descript, bef, link in zip(sales_names, descriptions, before, links):
        text = text + f"<b>{sale}</b> 📖\n<i>" + f"{descript}\n" + f"{bef} ⏳" + "\nhttps://book24.ru" + link + "</i>\n\n"

    await message.answer(f"{text}", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Читай-Город 🏢")
async def chit_gor_sales(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)

    sales = await parsers.scraper_chitay_gorod()

    sales_names = sales["sales"]
    descriptions = sales["descriptions"]
    before = sales["before"]
    links = sales["links"]

    text = "<b>Список акций в интернет-магазине Читай-Город 📚:</b>\n"

    for sale, descript, bef, link in zip(sales_names, descriptions, before, links):
        text = text + f"<b>{sale}</b> 📖\n<i>" + f"{descript}\n" + f"{bef} ⏳" + "\nhttps://www.chitai-gorod.ru/" + link + "</i>\n\n"

    await message.answer(f"{text}", reply_markup=ReplyKeyboardRemove())
