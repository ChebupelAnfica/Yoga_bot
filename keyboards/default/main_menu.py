from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обо мне🤲"),
            KeyboardButton(text="Йога💚")
        ],
        [
            KeyboardButton(text="Ответы на вопросы❔"),
            KeyboardButton(text="Служба заботы☎️")
        ],
        [
            KeyboardButton(text="Отзывы🤙"),
            KeyboardButton(text="Сбор данных⤵️")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите ниже."
)
