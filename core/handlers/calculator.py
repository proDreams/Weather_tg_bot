from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core import views
from core.utils.statesform import StepsForm
from core.keyboards.reply import choose_calc, choose_operation
from core.utils.calc import calc_init
from core.settings import custom_log


async def get_calc(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.choose_calc_type(), reply_markup=choose_calc())
    await state.set_state(StepsForm.GET_CALC_TYPE)


async def get_calc_type(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    if message.text == 'Рациональные':
        await state.update_data(calc_type='decimal')
        await message.answer(views.chosen_rational(), reply_markup=choose_operation())
        await state.set_state(StepsForm.GET_OPERATION)
    elif message.text == 'Комплексные':
        await state.update_data(calc_type='complex')
        await message.answer(views.chosen_complex(), reply_markup=choose_operation())
        await state.set_state(StepsForm.GET_OPERATION)
    elif message.text == 'Свободное выражение':
        await state.update_data(calc_type='free')
        await message.answer(views.chosen_freeform())
        await state.set_state(StepsForm.GET_EXPRESSION)
    else:
        await message.answer(views.wrong_calc_type())


async def get_operation(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    if message.text == 'a + b':
        await state.update_data(operation='+')
        op = 'сложения'
        await message.answer(views.got_operator(op), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StepsForm.GET_FIRST_NUM)
    elif message.text == 'a - b':
        await state.update_data(operation='-')
        op = 'вычитания'
        await message.answer(views.got_operator(op), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StepsForm.GET_FIRST_NUM)
    elif message.text == 'a * b':
        await state.update_data(operation='*')
        op = 'умножения'
        await message.answer(views.got_operator(op), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StepsForm.GET_FIRST_NUM)
    elif message.text == 'a / b':
        await state.update_data(operation='/')
        op = 'деления'
        await message.answer(views.got_operator(op), reply_markup=ReplyKeyboardRemove())
        await state.set_state(StepsForm.GET_FIRST_NUM)
    else:
        await message.answer(views.wrong_operator(), reply_markup=choose_operation())


async def get_first_num(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(first_num=message.text)
    await message.answer(views.enter_second_num())
    await state.set_state(StepsForm.GET_SECOND_NUM)


async def get_second_num(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(second_num=message.text)
    context_data = await state.get_data()
    result = calc_init(context_data)
    if result:
        await message.answer(f'Ответ: {context_data["first_num"]} {context_data["operation"]} '
                             f'{context_data["second_num"]} = {result}')
        await message.answer(views.end_calc())
        await state.clear()
    else:
        await message.answer(views.wrong_input())


async def get_expression(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(operation='')
    await state.update_data(expression=message.text)
    context_data = await state.get_data()
    await message.answer(f'{calc_init(context_data)}')
    await message.answer(views.end_calc())
    await state.clear()
