from src.imp import *
import psycopg2
from handlers import dp
from aiogram import executor
# logging.basicConfig(level=logging.INFO, filename='src/main.log', \
# filemode='w', format='%(asctime)s, %(levelname)s, %(message)s, %(name)s')
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    order_number = 1
    executor.start_polling(dp, skip_updates=True)




