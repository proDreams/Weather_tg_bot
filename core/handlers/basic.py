from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from core import views
from core.settings import custom_log


async def get_start(message: Message, bot: Bot):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.welcome_message(message.from_user.first_name), reply_markup=ReplyKeyboardRemove())
    await message.answer(views.welcome_message2(message.from_user.first_name))


async def get_help(message: Message, bot: Bot):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.help_message())


async def get_any(message: Message, bot: Bot):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.wrong_value_message())


async def get_about(message: Message, bot: Bot):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.about_message())
