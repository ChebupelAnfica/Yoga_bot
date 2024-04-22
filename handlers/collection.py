from distutils import command

from aiogram import F, types

from states.data_collection import Form

from aiogram.fsm.context import FSMContext

from loader import dp, bot

from database import SessionLocal

from aiogram.filters import StateFilter, Command

from models import People

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
import logging


@dp.message(StateFilter(None), F.text == 'Сбор данных⤵️')
async def collect_start(message: types.Message, state: FSMContext):
    try:
        await message.answer('Введите ваше полное имя.')
    except Exception as ex:
        logging.error(ex)

    try:
        await state.set_state(Form.fullname)
    except Exception as ex:
        logging.error(ex)


@dp.message(Form.fullname)
async def process_fullname(message: types.Message, state: FSMContext):
    try:
        await state.update_data(fullname=message.text)
    except Exception as ex:
        logging.error(ex)

    try:
        await message.answer("Теперь введите ваш номер телефона.")
    except Exception as ex:
        logging.error(ex)

    try:
        await state.set_state(Form.phone)
    except Exception as ex:
        logging.error(ex)


@dp.message(Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    try:
        await state.update_data(phone=message.text)
        user_data = await state.get_data()

        async with SessionLocal() as session:
            result = await session.execute(
                select(People).where(People.telegram_user_id == message.from_user.id))
            existing_user = result.scalars().first()

            if existing_user:
                existing_user.full_name = user_data['fullname']
                existing_user.phone_number = user_data['phone']
            else:
                new_user = People(telegram_user_id=message.from_user.id,
                                  full_name=user_data['fullname'],
                                  phone_number=user_data['phone'])
                session.add(new_user)

            await session.commit()
            await session.flush()

        await message.answer(
            text=f"Вас зовут: {user_data['fullname']}.\n"
                 f"Ваш номер телефона: {user_data['phone']}.\n"
                 f"Спасибо за предоставленную информацию!"
        )
        await state.clear()
    except SQLAlchemyError as e:
        await bot.send_message(chat_id=694834819, text=f"Произошла ошибка при работе с базой данных: {e}")
    except Exception as e:
        await bot.send_message(chat_id=694834819, text=f"Произошла неизвестная ошибка: {e}")
