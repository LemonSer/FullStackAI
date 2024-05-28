from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def menu():
    keyboard_1 = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton('Сгенерировать врага для сессии ДНД', callback_data='AI_DND')
    button_2 = InlineKeyboardButton('Сгенерировать изображение врага', callback_data='AI_IMG')
    button_3 = InlineKeyboardButton('Сгенерировать битву с врагом', callback_data='AI_BATLE')
    button_4 = InlineKeyboardButton('Сгенерирвать подходящие название врага', callback_data='AI_PROMT')
    keyboard_1.add(button_1, button_2, button_3, button_4)
    return keyboard_1