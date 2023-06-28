from src.imp import *
from src.config import ph_start

@dp.message_handler(commands="start", state="*")
async def command_start(message: types.Message, state: FSMContext):
    await state.update_data(orders=[])
    await bot.send_photo(photo=ph_start, caption=t.welcome, chat_id=message.from_user.id, reply_markup=kb.key_12345())
    await Wait.main_menu.set()

@dp.message_handler(commands="admin", state="*")
async def command_admin(message: types.Message, state: FSMContext):
    id = message.from_user.id
    if id not in admins: await message.answer("зря ты сюда пришел, воин, жми /start")
    else:
        await message.answer(t.admin_menu, reply_markup=kb.key_123())
        await Wait.admin_menu.set()

@dp.message_handler(commands="photo", state="*")
async def photo(message: types.Message, state: FSMContext):
    await message.answer("кидай фотку")
    await Wait.photo.set()

