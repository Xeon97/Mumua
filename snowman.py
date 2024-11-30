
# snowman.py

from .. import loader  # Импорт базового класса модулей
from telethon.tl.types import Message  # Тип сообщений

@loader.tds
class SnowmanMod(loader.Module):
    """Модуль для отправки эмодзи снеговика"""
    strings = {"name": "Snowman"}  # Название модуля

    async def снгcmd(self, message: Message):
        """Отправляет эмодзи снеговика"""
        await message.edit("☃️")  # Редактируем сообщение на эмодзи снеговика
