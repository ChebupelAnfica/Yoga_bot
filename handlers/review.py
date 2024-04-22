from aiogram import F, types
from aiogram.types import InputMediaPhoto

from keyboards.inline.inline_keyboard_markup import pay
from loader import dp, bot
import logging


@dp.message(F.text == "Отзывы🤙")
async def reviews(message: types.Message):
    photo_id1 = "AgACAgIAAxkBAAIBbWXATYXJGoTxrFtj7brD0QdnXz4jAAK_2zEb4DMAAUpuo_a87Xh2jwEAAwIAA3MAAzQE"
    photo_id2 = "AgACAgIAAxkBAAIBb2XATbu6OZDwusbp1z_15tl-d3Q9AALA2zEb4DMAAUr_7PKW3F-8QwEAAwIAA3MAAzQE"
    photo_id3 = "AgACAgIAAxkBAAIBcWXATcdKpNQUDouywurK3J4r4yLXAALB2zEb4DMAAUpGQ6j7of17MgEAAwIAA3MAAzQE"
    photo_id4 = "AgACAgIAAxkBAAIBc2XATc9Q_kBQ45aWwpGVtyohnzamAALC2zEb4DMAAUoRNmi8z8WNTQEAAwIAA3MAAzQE"
    photo_id5 = "AgACAgIAAxkBAAIBdWXATdvcSYtwxShJ9h4NUoO-TflAAALD2zEb4DMAAUrgZq_dvoZ7jwEAAwIAA3MAAzQE"
    media = [
        InputMediaPhoto(media=photo_id1),
        InputMediaPhoto(media=photo_id2),
        InputMediaPhoto(media=photo_id3),
        InputMediaPhoto(media=photo_id4),
        InputMediaPhoto(media=photo_id5)
    ]

    try:
        await bot.send_media_group(message.chat.id, media)
    except Exception as ex:
        logging.error(ex)

    try:
        await bot.send_message(message.chat.id, text='⬆️ Немного отзывов для ознакомления"',
                               reply_markup=pay)
    except Exception as ex:
        logging.error(ex)
