from aiogram import F, types

from keyboards.inline.inline_keyboard_markup import questions, back

from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging


@dp.message(F.text == "Ответы на вопросы❔")
async def question(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    await message.answer(f"❔ Часто задаваемые вопросы и ответы на них",
                         reply_markup=questions)


@dp.callback_query(F.data == 'questions1')
async def process_callback1(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Что в канале ❓
80+ сохранённых практики
+ занятия в прямом эфире 2 раза в неделю
(тоже сохраняются)
''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions2')
async def process_callback2(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Когда ❓

Прямые эфиры проходят
в среду 10:00
в пятницу 9:00

+ больше 80 практик в записи, по которым вы можете заниматься в любое удобное для вас время''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions3')
async def process_callback3(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Какой уровень ❓

Подойдёт и новичкам и опытным практикам.
Поверьте, будет интересно и плотно.
Это база, которую нужно пройти всем.''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions4')
async def process_callback4(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Сколько стоит ❓
        
2000₽ на целый месяц с доступом ко всем практикам и прямыми эфирами.''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions5')
async def process_callback5(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Что мне нужно для практик ❓

Место 2х2 метра и коврик.
''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions6')
async def process_callback6(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Длительность практик ❓

Занятия идут не больше часа (40-60 минут). Это удобно, потому что вам не нужно много времени, но вы успеваете проработать все на 100%.
Есть короткие практики на 25 минут.

Вы можете заниматься по разным практикам каждый день, можете 2 раза в неделю. Можете в записи, можете в прямом эфире.
''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions7')
async def process_callback7(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        if call.message:
            await bot.delete_message(chat_id=call.from_user.id,
                                     message_id=call.message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass

    try:
        await bot.send_message(chat_id=call.from_user.id, text='''Как ориентироваться в канале ❓

В канале есть хэштеги («руки», «растяжка», «кор», «балансы» и т.д.), чтобы вам было легко ориентироваться.
А еще есть хэштег «теория», по которому можно найти полезную информацию и два теоретических эфира.
''', reply_markup=back)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'back_to_all_questions')
async def process_back(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.edit_message_text('❓ Часто задаваемые вопросы и ответы на них',
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=questions)
    except Exception as ex:
        logging.error(ex)
