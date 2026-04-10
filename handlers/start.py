from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        text="Assalomu alaykum 👋\nMahsulotni tanlang:",
        reply_markup=main_menu()
    )