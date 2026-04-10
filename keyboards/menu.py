from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from products import PRODUCTS, DRINKS


def products_keyboard():
    buttons = [[KeyboardButton(text=name)] for name in PRODUCTS.keys()]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def drinks_keyboard():
    buttons = [[KeyboardButton(text=name)] for name in DRINKS.keys()]
    buttons.append([KeyboardButton(text="Ichimlik kerak emas")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def yes_no_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ha")],
            [KeyboardButton(text="Yo‘q")]
        ],
        resize_keyboard=True
    )


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Buyurtma berish")],
        ],
        resize_keyboard=True
    )

