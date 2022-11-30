from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core import views
from core.utils.statesform import StepsForm
from core.keyboards.reply import choose_weather, take_geo
from core.settings import custom_log
from core.utils.take_weather import init


async def get_weather_command(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.choose_weather_type(), reply_markup=choose_weather())
    await state.set_state(StepsForm.GET_WEATHER_TYPE)


async def get_weather_type(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    if message.text == 'По городу':
        await state.update_data(weather_type='find')
        await message.answer(views.chosen_city(), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StepsForm.BY_CITY)
    elif message.text == 'По геолокации\n(на смартфоне)':
        await state.update_data(weather_type='weather')
        await message.answer(views.chosen_geo(), reply_markup=take_geo())
        await state.set_state(StepsForm.BY_GEO)
    else:
        await message.answer(views.wrong_weather_type())

async def get_by_city(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(city=message.text)
    context_data = await state.get_data()
    result = init(context_data)
    if result == 0:
        await message.answer('Неправильный город, введите снова')
        await state.set_state(StepsForm.BY_CITY)
    else:
        await message.answer(result)
        await message.answer(views.end_weather())
        await state.clear()


async def get_by_geo(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(lat=message.location.latitude)
    await state.update_data(lon=message.location.longitude)
    context_data = await state.get_data()
    print(context_data)
    await message.answer(init(context_data))
    await message.answer(views.end_weather())
    await state.clear()
