from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    fullname = State()
    phone = State()
