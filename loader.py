from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(storage=MemoryStorage())
