from aiogram.utils.keyboard import ReplyKeyboardBuilder


def choose_weather():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='По городу')
    keyboard_builder.button(text='По геолокации\n(на смартфоне)')
    keyboard_builder.adjust(1, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')


def take_geo():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=True,
                                      input_field_placeholder='Выбери кнопку ↓')
