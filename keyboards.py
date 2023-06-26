from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

button_2 = [
    [
        InlineKeyboardButton(text='Подписаться', url='https://t.me/kkkkkkaktr')
    ],
    [
        InlineKeyboardButton(text='Подписаться', url='https://t.me/ttttxtxer')
    ],
    [
        InlineKeyboardButton(text='Подписался', callback_data='yes')
    ]
]
inline_kb1 = InlineKeyboardMarkup(inline_keyboard=button_2)

# items = ['Ответ 1', 'Ответ 2']
# current_answer_index = 0

# async def update():
#    keyboard = []
#    buttons = []
#    if current_answer_index > 0:
#        buttons.append(InlineKeyboardButton(text = 'Назад', callback_data = 'back'))
#    if current_answer_index < len(items) - 1:
#        buttons.append(InlineKeyboardButton(text = 'Вперед', callback_data = 'forward'))
#    keyboard.append(buttons)
#    return InlineKeyboardMarkup(inline_keyboard = keyboard)


button3 = [
    [
        InlineKeyboardButton(text='<', callback_data='back_'),
        InlineKeyboardButton(text='Выбрать', callback_data='var2'),
        InlineKeyboardButton(text='>', callback_data='next_ ')
    ]
]
inline_kb4 = InlineKeyboardMarkup(inline_keyboard=button3)


button4 = [
    [
        KeyboardButton(text='Подобрать займ'),
        KeyboardButton(text='Подобрать кредитную карту')
    ],
    [
        KeyboardButton(text='Подобрать кредит'),
        KeyboardButton(text='Служба поддержки')
    ]
]
default_kb2 = ReplyKeyboardMarkup(keyboard=button4, resize_keyboard=True)


# ЗАЙМ-ССЫЛКИ

button5 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb1 = InlineKeyboardMarkup(inline_keyboard=button5)


button6 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb2 = InlineKeyboardMarkup(inline_keyboard=button6)


button7 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb3 = InlineKeyboardMarkup(inline_keyboard=button7)


button8 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb4 = InlineKeyboardMarkup(inline_keyboard=button8)


button9 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb5 = InlineKeyboardMarkup(inline_keyboard=button9)


button10 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb6 = InlineKeyboardMarkup(inline_keyboard=button10)


button11 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb7 = InlineKeyboardMarkup(inline_keyboard=button11)


button12 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb8 = InlineKeyboardMarkup(inline_keyboard=button12)


button13 = [
    [
        InlineKeyboardButton(text='Взять займ!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
zaim_inline_kb9 = InlineKeyboardMarkup(inline_keyboard=button13)


button15 = [
    [
        KeyboardButton(text='')
    ]
]

# КАРТА-ССЫЛКИ

button16 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb1 = InlineKeyboardMarkup(inline_keyboard=button16)


button17 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb2 = InlineKeyboardMarkup(inline_keyboard=button17)


button18 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb3 = InlineKeyboardMarkup(inline_keyboard=button18)


button19 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb4 = InlineKeyboardMarkup(inline_keyboard=button19)


button20 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb5 = InlineKeyboardMarkup(inline_keyboard=button20)


button21 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb6 = InlineKeyboardMarkup(inline_keyboard=button21)


button22 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb7 = InlineKeyboardMarkup(inline_keyboard=button22)


button23 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb8 = InlineKeyboardMarkup(inline_keyboard=button23)


button24 = [
    [
        InlineKeyboardButton(text='Заказать карту!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
karta_inline_kb9 = InlineKeyboardMarkup(inline_keyboard=button24)


button30 = [
    [
        KeyboardButton(text='Назад')
    ],
    [
        KeyboardButton(text='Служба поддержки')
    ]
]
default_kb6 = ReplyKeyboardMarkup(keyboard=button30, resize_keyboard=True)


button40 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb1 = InlineKeyboardMarkup(inline_keyboard=button40)


button41 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb2 = InlineKeyboardMarkup(inline_keyboard=button41)


button42 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb3 = InlineKeyboardMarkup(inline_keyboard=button42)


button43 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb4 = InlineKeyboardMarkup(inline_keyboard=button43)


button44 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb5 = InlineKeyboardMarkup(inline_keyboard=button44)


button45 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb6 = InlineKeyboardMarkup(inline_keyboard=button45)


button46 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb7 = InlineKeyboardMarkup(inline_keyboard=button46)


button47 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb8 = InlineKeyboardMarkup(inline_keyboard=button47)


button48 = [
    [
        InlineKeyboardButton(text='Забрать деньги!', url='https://gl.guruleads.ru/click/9930/27')
    ]
]
kredit_inline_kb9 = InlineKeyboardMarkup(inline_keyboard=button48)


button30 = [
    [
        KeyboardButton(text='Назад')
    ],
    [
        KeyboardButton(text='Техническая поддержка')
    ]
]
default_kb6 = ReplyKeyboardMarkup(keyboard=button30, resize_keyboard=True)
