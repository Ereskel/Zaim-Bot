from aiogram import Bot, Dispatcher, Router
from config import token

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

router = Router()
