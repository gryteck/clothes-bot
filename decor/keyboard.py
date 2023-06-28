from aiogram import types


def key_123():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1", "2", "3"]
    return keyboard.add(*buttons)

def key_12345():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1", "2", "3", "4", "5"]
    return keyboard.add(*buttons)

def key_1234567():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["1", "2", "3", "4", "5", "6", "7"]
    return keyboard.add(*buttons)

def cont():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Продолжить"]
    return keyboard.add(*buttons)

def faq_inl():
    button_url = f't.me/+xGc7OhHeEaVjNzBi'
    markup = types.InlineKeyboardMarkup()
    return markup.add(types.InlineKeyboardButton(text="Наш канал", url=button_url))

def supp_inl():
    button_url = f't.me/caps_751'
    markup = types.InlineKeyboardMarkup()
    return markup.add(types.InlineKeyboardButton(text="Написать менеджеру", url=button_url))

def reviews_inl():
    button_url = f't.me/otzivy_caps_751'
    markup = types.InlineKeyboardMarkup()
    return markup.add(types.InlineKeyboardButton(text="Отзывы", url=button_url))

def write(id: int):
    button_url = f'tg://user?id={id}'
    markup = types.InlineKeyboardMarkup()
    return markup.add(types.InlineKeyboardButton(text="Связаться с покупателем", url=button_url))

def ok():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", "Нет"]
    return keyboard.add(*buttons)
