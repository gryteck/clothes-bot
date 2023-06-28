import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext


import decor.text as t
import decor.keyboard as kb
from src.wait import Wait

from src.config import bot, dp, supp_id, admins, ph_link, ph_size, ph_price

from src.order_num import order_num
from src.rate import rate
