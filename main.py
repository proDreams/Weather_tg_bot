import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from core.handlers.basic import get_start, get_help, get_any, get_about
from core.settings import settings, LOGFILE
from core.utils.commands import set_commands
from core.handlers import weather
from core.utils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - %(message)s",
                        )
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(weather.get_weather_command, Command(commands='weather'))
    dp.message.register(weather.get_weather_type, StepsForm.GET_WEATHER_TYPE)
    dp.message.register(weather.get_by_city, StepsForm.BY_CITY)

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(get_about, Command(commands='about'))
    dp.message.register(get_any)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        LOGFILE.close()


if __name__ == '__main__':
    asyncio.run(start())
