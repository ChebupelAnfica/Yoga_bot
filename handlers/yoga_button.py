from aiogram import F, types

from keyboards.inline.inline_keyboard_markup import pay

from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging


@dp.message(F.text == "Йога💚")
async def yoga(message: types.Message):
    try:
        await message.answer(f"""На канале безопасные практики, в которых нет лотосов и стоек на голове, но в то же время они за короткий срок построят мышечный корсет, подтянут ваше тело и разовьют гибкость.

На канале больше 120 записанных практик от 20 до 60 минут + 2 раза в неделю я провожу прямые эфиры, которые тоже сохраняются.

Практики на канале идут от легких к сложным, поэтому можно спокойно начинать заниматься даже если у вас нет опыта в йоге и вы считаете себя не гибким человеком.

Всему можно научиться практикуя на канале и задавая вопросы.

Если у вас возникает вопрос по технике выполнения, можно прислать фото асан в комментарии под любой практикой или просто описать свои ощущения. Я на все отвечаю.

С каким запросом можно прийти?
— болит спина/ шея
— встать на руки
— хочется исправить осанку
— наладить контакт с телом (понимать свои желания, ощущения)
— построить мышечный корсет, подтянув тело
— улучшить растяжку, раскрыть грудной отдел, тазобедренные
— научиться контролировать дыхание в жизни/ во время стрессовых ситуаций
— поднять эмоциональный фон в плюс
— наладить режим сна

и много чего ещё""", reply_markup=pay)
    except Exception as ex:
        logging.error(ex)


@dp.callback_query(F.data == 'trial_lesson')
async def process_callback_video_lesson(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_video(chat_id=callback_query.from_user.id,
                             video='BAACAgIAAxkBAAIEdmXBhZCkcfYYiRFpdSKOcysD4PtOAAIxSwAC4DMISozDxwpHNJWgNAQ')
        await bot.send_message(callback_query.from_user.id,
                               'Чтобы понять в каком формате проходят практики на канале, я предлагаю попробовать эту практику средней сложности, направленную на работу со спиной.')
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'monthly_subscription')
async def process_callback_video_subscription(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, '''Доступ на месяц стоит 2000 рублей.

Платеж списывается автоматически ежемесячно.

ℹ️ Чтобы оплатить доступ, воспользуйтесь кнопкой ниже.
ℹ️ Платеж обрабатывается автоматически''')
    except Exception as ex:
        logging.error(ex)
        pass
