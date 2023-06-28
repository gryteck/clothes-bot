from src.imp import *
from src.delivery import delivery
from src.config import ph_link, ph_size, ph_price

@dp.message_handler(state=Wait.order_start)
async def order_start(message: types.Message, state: FSMContext):
    if message.text not in ['1', '2', '3', '4', '5', '6', '7']:
        await message.answer(t.incorrect)
    id = message.from_user.id
    await state.update_data(type=message.text)
    await bot.send_photo(photo=ph_link, caption=t.send_link, chat_id=id, reply_markup=types.ReplyKeyboardRemove())
    await Wait.order_link.set()

@dp.message_handler(state=Wait.order_link)
async def order_link(message: types.Message, state: FSMContext):
    if (not message.text.startswith('http://')) and (not message.text.startswith('https://')):
        await message.answer('Неправильный формат ссылки, попробуйте снова')
        return
    await state.update_data(link=message.text)
    await bot.send_photo(photo=ph_size, caption=t.send_size, chat_id=message.from_user.id)
    await Wait.order_size.set()

@dp.message_handler(state=Wait.order_size)
async def order_size(message: types.Message, state: FSMContext):
    try:
        if 0 > int(message.text):
            await message.answer("Некорректный размер")
            return
    except(TypeError, ValueError):
        await message.answer("Некорректный размер")
        return
    a = await state.get_data()
    if a['type'] in ["6", "7"]: await message.answer("Если размера у товара не существует, просто отправьте 0")
    await state.update_data(size=message.text)
    await bot.send_photo(photo=ph_price, caption=t.send_price, chat_id=message.from_user.id)
    await Wait.order_price.set()

@dp.message_handler(state=Wait.order_price)
async def order_price(message: types.Message, state: FSMContext):
    r = float(rate.get())
    a = await state.get_data()
    await state.update_data(int_price=message.text)
    out_price = int(message.text)*r+delivery(a['type'])*0.8
    await state.update_data(out_price=str(out_price))
    a = await state.get_data()
    await message.answer(t.order(a), reply_markup=kb.ok())
    await Wait.order_correct.set()

@dp.message_handler(state=Wait.order_correct)
async def order_correct(message: types.Message, state: FSMContext):
    if message.text == "Да":
        a = await state.get_data()
        orders = a['orders']
        orders.append([a['link'], a['size'], a['int_price'], a['out_price']])
        await state.update_data(orders=orders)
        a = await state.get_data()
        print(a['orders'])
        await message.answer(text=t.orders(a), reply_markup=kb.key_123())
        await Wait.order_check.set()
    elif message.text == "Нет":
        await message.answer(text="Давайте заново")
        await message.answer(text=t.clothes_type, reply_markup=kb.key_1234567())
        await Wait.order_start.set()
    else:
        await message.answer(text=t.incorrect)
        return

@dp.message_handler(state=Wait.order_check)
async def order_check(message: types.Message, state: FSMContext):
    if message.text == "1":
        await message.answer("Укажите вид товара")
        await message.answer(t.clothes_type, reply_markup=kb.key_1234567())
        await Wait.order_start.set()
    elif message.text == "2":
        await message.answer(text=t.send_name)
        await Wait.order_name.set()
    elif message.text == "3":
        await state.update_data(orders=[])
        await message.answer(text=t.welcome, reply_markup=kb.key_12345())
        await Wait.main_menu.set()
    else:
        await message.answer(text=t.incorrect)
        return

@dp.message_handler(state=Wait.order_name)
async def order_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(t.send_address)
    await Wait.order_address.set()

@dp.message_handler(state=Wait.order_address)
async def order_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    id = message.from_user.id
    num = order_num.get()
    a = await state.get_data()
    await message.answer(t.order_num(num) + t.order_wait, reply_markup=kb.cont())
    # теперь админу
    await bot.send_message(text=t.order_num(num)+t.order_finish(a), chat_id=supp_id, reply_markup=kb.write(id))
    await Wait.start.set()


@dp.message_handler(state=Wait.order_finish, content_types=["photo"])
async def order_finish(message: types.Message, state: FSMContext):
    id = message.from_user.id
    check = message.photo[-1].file_id
    num = order_num.get()
    await state.update_data(check=check)
    a = await state.get_data()
    await bot.send_photo(photo=check, caption=t.order_num(num)+t.order_finish(a), chat_id=supp_id, reply_markup=kb.write(id))
    await message.answer(t.order_num(num)+t.order_wait)
