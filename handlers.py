import markups
import parsers

from aiogram.types import ReplyKeyboardRemove
from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter, CommandStart, CommandHelp, Command
from loader import dp


@dp.message_handler(CommandStart(), ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_start(message: types.Message):
    bot_name = await dp.bot.get_me()

    await message.answer(f"Привет, <b>{message.chat.username}</b>! "
                         f"<b>{bot_name.username}</b> - это бот "
                         f"для получения информации об актуальных скидках "
                         f"и акциях в интернет-магазинах книг "
                         f"<b>Читай Город</b>, <b>Book24</b> и "
                         f"<b>Лабиринт</b>.")


@dp.message_handler(CommandHelp(), ChatTypeFilter(types.ChatType.PRIVATE))
async def bot_help(message: types.Message):
    text = "<b>Список доступных команд:</b>\n" \
           "/help - вывести данные о командах.\n" \
           "/sales - посмотреть акции и скидки в выбранном " \
           "книжном интернет-магазине."

    await message.answer(text)


@dp.message_handler(Command("sales"), ChatTypeFilter(types.ChatType.PRIVATE))
async def book_sales(message: types.Message):
    await message.answer("Выберите книжный интернет-магазин, чтобы узнать об "
                         "актуальных скидках и акциях в нём 🎁", reply_markup=markups.menu)


@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), text="Book24 📙")
async def book24_sales(message: types.Message):
    sales = await parsers.scraper_book24()

    sales_names = sales["sales"]
    descriptions = sales["descriptions"]
    before = sales["before"]
    links = sales["links"]

    text = "<b>Список акций в интернет-магазине book24 📚:</b>\n"

    for sale, descript, bef, link in zip(sales_names, descriptions, before, links):
        text = text + f"<b>{sale}</b> 📖\n<i>" + f"{descript}\n" + f"{bef} ⏳" + "\nhttps://book24.ru" + link + "</i>\n\n"

    await message.answer(f"{text}", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), text="Читай-Город 🏢")
async def chit_gor_sales(message: types.Message):
    sales = await parsers.scraper_chitay_gorod()

    sales_names = sales["sales"]
    descriptions = sales["descriptions"]
    before = sales["before"]
    links = sales["links"]

    text = "<b>Список акций в интернет-магазине Читай-Город 📚:</b>\n"

    for sale, descript, bef, link in zip(sales_names, descriptions, before, links):
        text = text + f"<b>{sale}</b> 📖\n<i>" + f"{descript}\n" + f"{bef} ⏳" + "\nhttps://www.chitai-gorod.ru/" + link + "</i>\n\n"

    await message.answer(f"{text}", reply_markup=ReplyKeyboardRemove())
