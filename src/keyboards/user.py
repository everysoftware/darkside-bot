from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)
from aiogram.types.web_app_info import WebAppInfo


main_kb = [
    [KeyboardButton(text='Сделать заказ', web_app=WebAppInfo(url='https://everysoftware.github.io/'))],
    [KeyboardButton(text='Автор бота')]
]

# Передать информацию из сайта в тг можно только через Reply-клавиатуру,
# но при этом сайт не видит наших данных. В Inline-клавиатуре всё наоборот.
# Почему и зачем тг так сделали - одному Богу известно.
main = ReplyKeyboardMarkup(
    keyboard=main_kb,
    # Чтобы прилично выглядеть на телефоне.
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)
