from src.imp import *
import asyncio

@dp.message_handler(state=Wait.main_menu)
async def main_menu(message: types.Message, state: FSMContext):
    id = message.from_user.id
    if message.text == "1":
        await message.answer("Укажите вид товара")
        await message.answer(t.clothes_type, reply_markup=kb.key_1234567())
        await Wait.order_start.set()
    elif message.text == "2":
        await message.answer("Укажите вид товара")
        await message.answer(t.clothes_type, reply_markup=kb.key_1234567())
        await Wait.calculator_start.set()
    elif message.text == "3":
        await message.answer("Вы можете ознакомиться с отзывами здесь", reply_markup=kb.reviews_inl())
        await asyncio.sleep(1)
        await message.answer("Продолжить?", reply_markup=kb.cont())
        await Wait.start.set()
    elif message.text == "4":
        await message.answer(t.info, reply_markup=kb.faq_inl(), parse_mode=types.ParseMode.HTML)
        await asyncio.sleep(1)
        await message.answer("Продолжить?", reply_markup=kb.cont())
        await Wait.start.set()
    elif message.text == "5":
        await message.answer("Обращаться только по важным вопросам!", reply_markup=kb.supp_inl())
        await asyncio.sleep(1)
        await message.answer("Продолжить?", reply_markup=kb.cont())
        await Wait.start.set()
    else:
        await message.answer(t.incorrect, reply_markup=kb.key_12345())
        return

@dp.message_handler(state=Wait.start)
async def start(message: types.Message, state: FSMContext):
    if message.text == "Продолжить":
        await state.update_data(orders=[])
        await message.answer(text=t.welcome, reply_markup=kb.key_12345())
        await Wait.main_menu.set()
    else:
        await message.answer(t.incorrect)
        return

@dp.message_handler(state=Wait.photo, content_types=["photo"])
async def photo(message: types.Message, state: FSMContext):
    id = message.from_user.id
    ph_id = message.photo[-1].file_id
    await message.answer(ph_id)
    await Wait.photo.set()
