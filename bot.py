from aiogram import Bot, Dispatcher, types
from aiogram import F
import asyncio
import logging


logging.basicConfig(level=logging.INFO)
API_TOKEN = '8128564762:AAEV6TADhd_U6bovm1fiPXjNKgMp6daCDOs'

# Список ключевых слов для фильтрации
spam_keywords = ['доход', 'заработок']

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(F.text)
async def filter_spam(message: types.Message):
    # Проверка на наличие ключевых слов в сообщении
    if any(keyword in message.text.lower() for keyword in spam_keywords):
        await message.delete()  # Удаление сообщения
        print(f"Удалено сообщение от {message.from_user.full_name}: {message.text}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
