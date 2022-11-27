from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_WEATHER_TYPE = State()
    BY_CITY = State()
    BY_GEO = State()
