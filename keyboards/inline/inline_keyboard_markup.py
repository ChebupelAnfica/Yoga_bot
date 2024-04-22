from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

questions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Что в канале ❔", callback_data="questions1")
        ],
        [
            InlineKeyboardButton(text="Когда ❔", callback_data="questions2")
        ],
        [
            InlineKeyboardButton(text="Какой уровень ❔", callback_data="questions3")
        ],
        [
            InlineKeyboardButton(text="Сколько стоит ❔", callback_data="questions4")
        ],
        [
            InlineKeyboardButton(text="Что нужно для практики ❔", callback_data="questions5")
        ],
        [
            InlineKeyboardButton(text="Длительность практик ❔", callback_data="questions6")
        ],
        [
            InlineKeyboardButton(text="Как ориентироваться в канале ❔", callback_data="questions7")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="cancel")
        ]
    ],
)

back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👈", callback_data="back_to_all_questions")
        ]
    ]
)

pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пробное занятие", callback_data='trial_lesson')
        ],
        [
            InlineKeyboardButton(text="Ежемесечная подписка", callback_data='monthly_subscription')
        ],
        [
            InlineKeyboardButton(text="Купить подписку на месяц(1590₽)",
                                 url="https://sashaumorya.payform.ru/?invoice_id=2ef48250c6673c92891e287594296854&paylink=1")
        ]
    ]
)

pay_trial = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ежемесечная подписка", callback_data='monthly_subscription')
        ],
        [
            InlineKeyboardButton(text="Купить подписку на месяц(1590₽)",
                                 url="https://sashaumorya.payform.ru/?invoice_id=2ef48250c6673c92891e287594296854&paylink=1")
        ]
    ]
)
