import os, asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()
TOKEN=os.getenv('BOT_TOKEN')
URL=os.getenv('WEBAPP_URL','')
dp=Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    k=InlineKeyboardBuilder()
    if URL:
        k.add(InlineKeyboardButton(text='💀 ВОЙТИ В ИГРУ', web_app=WebAppInfo(url=URL)))
    else:
        k.button(text='🌍 🇺🇦 Українська', callback_data='lang_uk')
        k.button(text='🌍 🇷🇺 Русский', callback_data='lang_ru')
        k.button(text='🌍 🇬🇧 English', callback_data='lang_en')
    await message.answer('💀 ВМОГИЛЕ\n\nВыбери язык / Обери мову / Choose language:', reply_markup=k.as_markup())

async def main():
    if not TOKEN: raise RuntimeError('BOT_TOKEN is missing')
    await dp.start_polling(Bot(TOKEN))

if __name__=='__main__': asyncio.run(main())
