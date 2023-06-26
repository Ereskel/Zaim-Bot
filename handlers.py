import asyncio

from aiogram.fsm.context import FSMContext

from keyboards import karta_inline_kb9, default_kb6, kredit_inline_kb1, kredit_inline_kb2, kredit_inline_kb3, \
    kredit_inline_kb4, kredit_inline_kb5, kredit_inline_kb6, kredit_inline_kb7, kredit_inline_kb8, kredit_inline_kb9
from loader import dp, Bot, router, bot
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.types import Message, CallbackQuery
from aiogram import types
from config import channel1, channel2
from keyboards import default_kb2, zaim_inline_kb1, zaim_inline_kb2, zaim_inline_kb3, zaim_inline_kb4, zaim_inline_kb5, \
    zaim_inline_kb6, zaim_inline_kb7, zaim_inline_kb8, zaim_inline_kb9, karta_inline_kb1, karta_inline_kb2, \
    karta_inline_kb3, \
    karta_inline_kb4, karta_inline_kb5, karta_inline_kb6, karta_inline_kb7, karta_inline_kb8
from state import Zaim


def check_sub_channel(chat_member):
    print(chat_member.status)
    if chat_member.status != 'left':
        return True
    else:
        return False


@router.message(Command('start'))
async def command_start(message: types.Message, state: FSMContext):
    a = check_sub_channel(await bot.get_chat_member(chat_id=channel1, user_id=message.from_user.id))
    b = check_sub_channel(await bot.get_chat_member(chat_id=channel2, user_id=message.from_user.id))
    if a and b:
        await bot.send_message(message.from_user.id,
                               'Выберите интересующий вас продукт.\n\n Для перезапуска бота нажмите /start',
                               reply_markup=default_kb2)
        await state.set_state(Zaim.state)
    else:
        await bot.send_message(message.from_user.id,
                               'Чтобы воспользоваться полным функционалом бота подпишитесь на данные'
                               'каналы и нажмите "Готово"',
                               reply_markup=default_kb2)


@router.callback_query(Text('yes'))
async def handler2(callback: CallbackQuery, state: FSMContext):
    print(callback.message.from_user.id)
    #  await bot.delete_message(callback.message.from_user.id, callback.message.message_id)
    a = check_sub_channel(await bot.get_chat_member(chat_id=channel1, user_id=callback.from_user.id))
    b = check_sub_channel(await bot.get_chat_member(chat_id=channel2, user_id=callback.from_user.id))
    if a and b:
        await bot.send_message(callback.from_user.id,
                               'Выберите интересующий вас продукт.\n\n Для перезапуска бота нажмите /start')
        await state.set_state(Zaim.state)
    else:
        await bot.send_message(callback.from_user.id, 'В доступе отказано. Подпишитесь на все каналы.')


# @router.callback_query(lambda c: c.data.startswith(('back_', 'next_')))
# async def navigate(callback: CallbackQuery):
#    page = int(callback.data.split('_')[-1])
#    await bot.edit_message_reply_markup(callback.message.chat.id,
#                                        callback.message.message_id)


@router.message(Text('Подобрать займ'))
async def handler4(message: Message, state: FSMContext):
    message_id = message.message_id
    sent_message = await bot.send_message(message.chat.id, '⏳ Подбираем займ для вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⌛️ Подбираем займ для вас..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⏳ Подбираем займ для вас...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Подбираем займ для вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово..')
    await asyncio.sleep(1)
    await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
    await bot.send_message(chat_id=sent_message.chat.id, text='️Успешно! Займ подобран!', reply_markup=default_kb6)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb1)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb2)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb3)
    await asyncio.sleep(1)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb4)
    await asyncio.sleep(6)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb5)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb6)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb7)
    await asyncio.sleep(5)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb8)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=zaim_inline_kb9)


@router.message(Text('Подобрать кредитную карту'), )
async def handler4(message: Message):
    message_id = message.message_id
    sent_message = await bot.send_message(message.chat.id, '⏳ Подбираем кредитную карту для Вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⌛️ Подбираем кредитную карту для Вас..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⏳ Подбираем кредитную карту для Вас...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Подбираем кредитную карту для Вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово..')
    await asyncio.sleep(1)
    await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
    await bot.send_message(chat_id=sent_message.chat.id, text='️Успешно! Кредитная карта подобрана!',
                           reply_markup=default_kb6)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb1)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb2)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb3)
    await asyncio.sleep(1)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb4)
    await asyncio.sleep(6)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb5)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb6)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb7)
    await asyncio.sleep(5)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb8)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=karta_inline_kb9)


@router.message(Text('Подобрать кредит'))
async def handler4(message: Message):
    message_id = message.message_id
    sent_message = await bot.send_message(message.chat.id, '⏳ Подбираем лучшее предложение для Вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⌛️ Подбираем лучшее предложение для Вас..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='⏳ Подбираем лучшее предложение для Вас...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Подбираем лучшее предложение для Вас.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово..')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово...')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⏳ Почти готово.')
    await asyncio.sleep(1)
    await bot.edit_message_text(chat_id=sent_message.chat.id, message_id=sent_message.message_id,
                                text='️⌛️ Почти готово..')
    await asyncio.sleep(1)
    await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
    await bot.send_message(chat_id=sent_message.chat.id, text='️Успешно! Вот лучшие предложения!',
                           reply_markup=default_kb6)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb1)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb2)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb3)
    await asyncio.sleep(1)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb4)
    await asyncio.sleep(6)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb5)
    await asyncio.sleep(3)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb6)
    await asyncio.sleep(4)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb7)
    await asyncio.sleep(5)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb8)
    await asyncio.sleep(2)
    await message.answer('1️⃣ Займер ✅\n'
                         "🔥Рекомендуем🔥\n"
                         'Первый займ 0% без скрытых комиссий\n'
                         'Процентная ставка: от 0% до 1% в день.\n'
                         'Сумма займа от 2 000 до 30 000 рублей.\n'
                         'Срок займа: от 7 до 30 дней\n', reply_markup=kredit_inline_kb9)


@router.message(Text('Назад'))
async def handler_20(message: Message):
    await message.answer('Выберите интересующий вас продукт.\n\n Для перезапуска бота нажмите /start',
                         reply_markup=default_kb2)


@router.message(Text('Служба поддержки'))
async def handler_21(message: Message):
    await message.answer('Напишите вот суда.')

# @router.message(Text('Подобрать кредитную карту'))


# @router.message(Text(''))

# @router.callback_query(text="subchanneldone")
# async def subchanneldone(message: types.Message):
#    await bot.delete_message(message.from_user.id, message.message.message_id)
#    if ((check_sub_channel1(await bot.get_chat_member(chat_id=channel1, user_id=message.from_user.id)) and
#         ((check_sub_channel1(await bot.get_chat_member(chat_id=channel2, user_id=message.from_user.id)))))):

#        await bot.send_message(message.from_user.id,
#                               'Выберите свою возрастную категорию, {0.first_name}'.format(message.from_user),
#                               reply_markup=inline_kb_1)
#    if check_sub_channel1(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
#       await bot.send_message(message.from_user.id, 'Выберите свою возрастную категорию, {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)
#    else:
#        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=inline_kb_1)
