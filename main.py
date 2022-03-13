from PIL import Image
import requests
from io import BytesIO
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import hashlib
import urllib3
import urllib.request
from urllib.request import Request, urlopen

bot = Bot(token="5225895779:AAGfc3PNt3z4Cssi-UssiQY8psJeQeMaJSU", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class sms13(StatesGroup):
    sms_text = State()
baza = []
povtor = []
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("<b>Закинь список адресов....</b>")
    await sms13.sms_text.set()

    @dp.message_handler(state=sms13.sms_text)
    async def widjet(message: Message,  state: FSMContext):
        url = message.text
        pp = url.split()
        i = 0
        z = 0
        s = len(pp)
        dd = await message.answer(f"<b>Проверяю {s} ссылок ожидай ....</b>")
        while i <= s:
            try:
                resource = urllib.request.urlopen(pp[i])
                await dd.edit_text(f"<b>Проверяю Ссылку №{i}</b>")
                out = open("img.jpg", 'wb')
                out.write(resource.read())
                out.close()
                tt = open("img.jpg", "rb").read()
                hash_object = hashlib.md5(tt)
                xx = hash_object.hexdigest()

               
                
                if xx  not  in baza:
                    baza.append(xx)
                    
                    i = i + 1
                else:
                    await message.answer(f"<b>Ссылка дубль <code>{pp[i]}</code></b>")
                    z = z + 1
                    i = i + 1
            except:
                  break 
        #gg = 
        await message.answer(
                    f"<b>Сылки Дублей {z} шт</b>")


if __name__ == "__main__":
    executor.start_polling(dp)
