from aiogram import executor
from loader import dp
import middlewares, filters, handlers


if __name__ == '__main__':
    executor.start_polling(dp)
