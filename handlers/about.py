from aiogram import F, types

from keyboards.inline.close import close_inline_keyboard
from loader import dp, bot
import logging


@dp.message(F.text == "Обо мне🤲")
async def send_photo(message: types.Message):
    photo_id = "AgACAgIAAxkBAAPCZcA_mGwhwl1yKoXRiCIt9HcYgEsAArjbMRvgMwABSmCEbWsEqpK1AQADAgADcwADNAQ"
    try:
        await bot.send_photo(message.chat.id, photo_id, caption=f"""Я преподаю и практикую йогу более 2-х лет. С 6 лет я занималась спортом, но придя в йогу мое физическое и эмоциональное состояние было на нуле.

Регулярные практики построили мое тело и помогли мне стать решительнее и сильнее.

За этот короткий срок я безопасно пришла к тем результатам, которые у меня есть:
— различные балансы на руках
— гибкость
— спокойное эмоциональное состояние
и другие красивые асаны, которые вы можете увидеть в моем инстаграме.

Я практикую и преподаю по определенной методологии (FYSM) и именно благодаря ей вы можете видеть такой быстрый рост у меня и людей, которые со мной занимаются.

Я уверена, что йога меняет жизнь на «до» и «после», особенно если заниматься ей регулярно. Именно поэтому я решила отучиться на преподавателя и предлагаю вам самый удобный для этого способ — телеграмм канал с огромным количеством практик.""",
                             reply_markup=close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
