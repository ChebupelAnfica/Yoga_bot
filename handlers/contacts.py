from aiogram import F, types

from keyboards.inline.close import close_inline_keyboard
from loader import dp, bot
import logging


@dp.message(F.text == 'Служба заботы☎️')
async def contact(message: types.Message):
    try:
        await message.answer("При любых трудностях о вас всегда позаботятся тут @chebupanfica",
                             reply_markup=close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
