import logging

from aiogram import F, types

import keyboards.inline.close

from loader import dp, bot


@dp.message(F.text == 'Кнопка меню')
async def main_menu_handler(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except:
        pass
    try:
        await bot.send_message(message.from_user.id, 'Обработал',
                               reply_markup=keyboards.inline.close.close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
        pass
