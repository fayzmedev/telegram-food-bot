from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.menu import products_keyboard, drinks_keyboard, yes_no_keyboard
from products import PRODUCTS, DRINKS
from config import config
from database import add_order

router = Router()


# ================= STATES =================
class OrderState(StatesGroup):
    choosing_product = State()
    choosing_quantity = State()
    choosing_drink = State()
    waiting_for_address = State()
    waiting_for_payment = State()


# ================= START =================
@router.message(F.text == "Buyurtma berish")
async def start_order(message: Message, state: FSMContext):
    await message.answer("Mahsulot tanlang:", reply_markup=products_keyboard())
    await state.set_state(OrderState.choosing_product)


# ================= PRODUCT =================
@router.message(OrderState.choosing_product)
async def choose_product(message: Message, state: FSMContext):
    product = message.text

    if product not in PRODUCTS:
        await message.answer("Iltimos tugmalardan tanlang.")
        return

    await state.update_data(product=product)
    await state.set_state(OrderState.choosing_quantity)
    await message.answer("Nechta buyurtma qilasiz?")


# ================= QUANTITY =================
@router.message(OrderState.choosing_quantity)
async def choose_quantity(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Iltimos son kiriting.")
        return

    await state.update_data(quantity=int(message.text))
    await state.set_state(OrderState.choosing_drink)
    await message.answer("Ichimlik ham olasizmi?", reply_markup=yes_no_keyboard())


# ================= DRINK =================
@router.message(OrderState.choosing_drink)
async def choose_drink(message: Message, state: FSMContext):
    text = message.text

    if text == "Ha":
        await message.answer("Ichimlik tanlang:", reply_markup=drinks_keyboard())
        return

    if text == "Yo‘q":
        await state.update_data(drink=None)
        await state.set_state(OrderState.waiting_for_address)
        await message.answer("Manzilingizni yozing:")
        return

    if text in DRINKS:
        await state.update_data(drink=text)
        await state.set_state(OrderState.waiting_for_address)
        await message.answer("Manzilingizni yozing:")
        return

    await message.answer("Tugmalardan foydalaning.")


# ================= ADDRESS =================
@router.message(OrderState.waiting_for_address)
async def get_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()

    product = data["product"]
    quantity = data["quantity"]
    drink = data.get("drink")

    total = PRODUCTS[product] * quantity
    if drink:
        total += DRINKS[drink]

    # TOTAL ni state ichiga saqlaymiz
    await state.update_data(total=total)

    text = f"📦 Buyurtma:\n\n"
    text += f"🍔 {product} x {quantity} = {PRODUCTS[product] * quantity} so'm\n"

    if drink:
        text += f"🥤 {drink} = {DRINKS[drink]} so'm\n"

    text += f"\n📍 Manzil: {data['address']}"
    text += f"\n\n💰 Jami: {total} so'm"
    text += "\n\n💳 To‘lov uchun karta:\n8600 1234 5678 9012"
    text += "\n\nChekni yuboring."

    await message.answer(text)
    await state.set_state(OrderState.waiting_for_payment)


# ================= PAYMENT =================
@router.message(OrderState.waiting_for_payment, F.photo)
async def get_payment(message: Message, state: FSMContext):
    data = await state.get_data()

    # DB ga yozamiz
    add_order(
        user_id=message.from_user.id,
        product=data["product"],
        quantity=data["quantity"],
        drink=data.get("drink"),
        address=data["address"],
        total=data["total"]
    )

    caption = (
        "🆕 YANGI BUYURTMA!\n\n"
        f"👤 User ID: {message.from_user.id}\n"
        f"🍔 Mahsulot: {data['product']}\n"
        f"🔢 Soni: {data['quantity']}\n"
        f"🥤 Ichimlik: {data.get('drink')}\n"
        f"📍 Manzil: {data['address']}\n"
        f"💰 Jami: {data['total']} so'm"
    )

    await message.bot.send_photo(
        chat_id=config.ADMIN_ID,
        photo=message.photo[-1].file_id,
        caption=caption
    )

    await message.answer("✅ Buyurtmangiz qabul qilindi!")
    await state.clear()