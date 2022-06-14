from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


book24_btn = KeyboardButton("Book24 📙")
chitgor_btn = KeyboardButton("Читай-Город 🏢")

menu = ReplyKeyboardMarkup(resize_keyboard=True)

menu.add(book24_btn, chitgor_btn)
