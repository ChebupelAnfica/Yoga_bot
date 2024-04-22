import logging

from aiogram import types, F
from aiogram.filters import Command, CommandObject

import keyboards
from data.config import ADMINS
from database import SessionLocal
from loader import dp, bot
from utils.db.queries import get_user, create_user
from aiogram.fsm.context import FSMContext
from states.data_collection import Form


@dp.message(Command("start"))
# @dp.message(CommandStart(deep_link=True))
async def cmd_start(message: types.Message,
                    command: CommandObject,
                    state: FSMContext):
    try:
        async with SessionLocal.begin() as session:
            user = await get_user(session,
                                  message.from_user.id)
            if user is None:
                await create_user(session,
                                  message.from_user.id,
                                  message.from_user.username,
                                  message.from_user.full_name)
            # session.commit()  # БОЛЬШЕ НЕ ИСПОЛЬЗУЕМ. АВТОКОММИТ РАБОТАЕТ
    except Exception as ex:
        logging.error(ex)
        try:
            await bot.send_message(message.from_user.id, '''Произошла ошибка. Начните с начала -> /start''')
        except Exception as ex:
            logging.error(ex)
        return
    if command.args:
        if command.args == '777':
            await message.answer('Введите ваше полное имя.')
            await state.set_state(Form.fullname)
            return
    try:
        await bot.send_message(message.from_user.id, f'''<b>Привет, {message.from_user.full_name}</b>👋\n                                
Меня зовут Мия.
Я преподаю йогу по методологии <b><i>FYSM</i></b> в <u>закрытом телеграмм канале «ЙОГА У МОРЯ».</u>

Там есть практики в записи и в прямом эфире.

Здесь вы можете <i>оформить подписку на канал и начать заниматься вместе со мной.</i> ''',
                               reply_markup=keyboards.default.main_menu.main_menu)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.message(F.content_type.in_({'photo', 'video'}))
async def echo_files(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        try:
            await bot.send_message(message.from_user.id, message.photo[0].file_id)
        except:
            await bot.send_message(message.from_user.id, message.video.file_id)
        return
