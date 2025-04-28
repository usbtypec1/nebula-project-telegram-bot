from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router(name=__name__)


@router.message(CommandStart())
async def on_start(message: Message) -> None:
    await message.answer_photo(
        photo="AgACAgIAAxkBAAMmaA9dNH4jTme5Q89m2MC2hQXVPyYAAm3xMRs1ZYFIcdAWbgyw208BAAMCAAN5AAM2BA",
        caption="👇 Нажмите на кнопку чтобы запустить приложение.",
    )
