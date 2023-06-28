from aiogram.dispatcher.filters.state import State, StatesGroup


class Wait(StatesGroup):
    main_menu = State()

    start = State()

    order_start = State()
    order_photo = State()
    order_link = State()
    order_size = State()
    order_price = State()
    order_correct = State()
    order_check = State()
    order_name = State()
    order_address = State()
    order_finish = State()

    calculator_start = State()
    calculator_price = State()

    admin_menu = State()
    admin_rate = State()
    admin_number = State()
    admin_card = State()

    photo = State()

