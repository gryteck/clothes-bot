from src.imp import *

@dp.message_handler(state=Wait.admin_menu)
async def admin_menu(message: types.Message, state: FSMContext):
    if message.text == "1":
        await message.answer(f"Текущий курс: {str(rate.get())}\n\nКакой установить курс?")
        await Wait.admin_rate.set()
    elif message.text == "2":
        await message.answer(f"Текущий номер: {str(order_num.get())}\n\nКакой установить номер заказа?")
        await Wait.admin_number.set()
    elif message.text == "3":
        await message.answer(f"че.")
        return

@dp.message_handler(state=Wait.admin_rate)
async def admin_rate(message: types.Message, state: FSMContext):
    try:
        if 5.0 > float(message.text) or float(message.text) > 30.0:
            await message.answer("Некорректный курс, давай снова")
            return
    except(TypeError, ValueError):
        await message.answer("Некорректный курс, давай снова")
        return
    num = rate.upd(float(message.text))
    await message.answer(f'Курс обновлен до {str(num)}')

@dp.message_handler(state=Wait.admin_number)
async def admin_number(message: types.Message, state: FSMContext):
    try:
        if 0 > int(message.text):
            await message.answer("Некорректный номер, давай снова")
            return
    except(TypeError, ValueError):
        await message.answer("Некорректный номер, давай снова")
        return
    num = order_num.upd(int(message.text))
    await message.answer(f'Номер обновлен до {str(num)}')

