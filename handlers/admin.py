from aiogram import Router, F
from aiogram.types import Message
from config import config
from database import get_monthly_stats

router = Router()


@router.message(F.text == "/stats")
async def monthly_stats(message: Message):
    if message.from_user.id != config.ADMIN_ID:
        return

    stats = get_monthly_stats()

    if not stats:
        await message.answer("Statistika yo‘q.")
        return

    text = "📊 Oylik statistika:\n\n"

    for month, total_orders, total_income in stats:
        text += f"📅 {month}\n"
        text += f"🛒 Buyurtmalar: {total_orders}\n"
        text += f"💰 Daromad: {total_income} so'm\n\n"

    await message.answer(text)