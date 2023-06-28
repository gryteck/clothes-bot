from src.imp import *
from src.delivery import delivery
from src.config import ph_price

@dp.message_handler(state=Wait.calculator_start)
async def calculator_start(message: types.Message, state: FSMContext):
    if message.text not in ['1', '2', '3', '4', '5', '6', '7']:
        await message.answer(t.incorrect)
    await state.update_data(type=message.text)
    id = message.from_user.id
    await bot.send_photo(photo=ph_price, caption=t.send_price, chat_id=id, reply_markup=types.ReplyKeyboardRemove())
    await Wait.calculator_price.set()

@dp.message_handler(state=Wait.calculator_price)
async def calculator_price(message: types.Message, state: FSMContext):
    r = float(rate.get())
    a = await state.get_data()
    out_price = int(message.text)*r+delivery(a['type'])*0.8
    await message.answer(f"Цена - {str(out_price)} рублей", reply_markup=kb.cont())
    await Wait.start.set()
