from aiogram.types import (Message,
                           LabeledPrice,
                           ContentType,
                           PreCheckoutQuery,
                           ShippingQuery,
                           ShippingOption
                           )
from aiogram import F

from src.app import bot, dp, db
from src.config import Config
from src.messages.payments import MESSAGES


@dp.message(F.content_type == ContentType.WEB_APP_DATA)
async def buy_process(msg: Message) -> None:
    prod_id = msg.web_app_data.data
    if prod_id.isnumeric():
        prod_id = int(prod_id)
        if db.product_exists(prod_id):
            prod = db.get_product(prod_id)[0]
            price = [LabeledPrice(label=prod[2], amount=prod[3] * 100)]
        else:
            await msg.answer(MESSAGES.get('wrong_product_info'))
            return
    else:
        await msg.answer(MESSAGES.get('wrong_product_info'))
        return

    await msg.answer_invoice(
        title='Оплата заказа',
        description=price[0].label,
        provider_token=Config.pay_token,
        currency='rub',
        need_email=True,
        need_phone_number=True,
        prices=price,
        start_parameter='example',
        payload='some_invoice',
        is_flexible=True
    )


def check_validity(query: ShippingQuery) -> bool:
    valid_cities = {
        'нижний новгород',
        'арзамас',
        'санкт-петербург',
        'сочи',
        'москва',
        'бор',
        'дзержинск',
        'киров'
    }
    return query.shipping_address.country_code == 'RU' and \
        query.shipping_address.city.lower() in valid_cities


SHIPPING_PRICES = {
    'regular': [LabeledPrice(label='Обычная доставка', amount=0 * 100)],
    'fast': [LabeledPrice(label='Быстрая доставка', amount=100 * 100)],
}

SHIPPING_OPTIONS = [
    ShippingOption(id='regular', title='Обычная (1-2 ч)', prices=SHIPPING_PRICES['regular']),
    ShippingOption(id='fast', title='Быстрая (45 мин)', prices=SHIPPING_PRICES['fast'])
]


@dp.shipping_query(lambda query: True)
async def shipping_process(query: ShippingQuery) -> None:
    if not check_validity(query):
        await query.answer(
            ok=False,
            error_message=MESSAGES.get('no_delivery').format(query.shipping_address.city)
        )
        return

    await query.answer(
        ok=True,
        shipping_options=SHIPPING_OPTIONS,
    )


@dp.pre_checkout_query(lambda query: True)
async def pre_checkout_process(pre_checkout: PreCheckoutQuery) -> None:
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


@dp.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(msg: Message) -> None:
    await msg.answer(MESSAGES.get('order_accepted'))
