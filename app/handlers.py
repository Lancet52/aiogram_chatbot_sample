from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router_handlers = Router()


@router_handlers.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'ТЕКСТ ПРИВЕТСТВИЯ')


@router_handlers.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply('ПОМОЩЬ')


@router_handlers.message(F.text)
async def hello(message: Message):
    if message.text.lower()=='привет':
        await message.reply('ПРИВЕТ!')
