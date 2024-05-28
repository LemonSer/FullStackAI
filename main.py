from config import TELEGRAM_TOKEN
from aiogram import Bot, Dispatcher, types, executor
from neiro.text import get_response
from neiro.test import general_img
from  keyboard.inlinekeyboard import menu
from neiro.battle import get_battle
from neiro.dnd import get_dnd


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда запуска бота'),
        types.BotCommand(command='/get_battle', description='Cгенерировать битву'),
        types.BotCommand(command='/get_dnd', description='Cгенерировать врага для ДНД'),
        types.BotCommand(command='/general_img', description='Сгенерировать изображение'),
        types.BotCommand(command='/get_response', description='Cгенерировать промпт'),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def func_start(message: types.Message):
    await message.answer('Привет я твой нейросотрудник, который может помочь тебе с следующими задачами: Сгенерировать изображение(/general_img: название), '
                         'сгенерировать врага для ДНД(/get_dnd: название), сгенерировать промпт(/get_response: название), сгенерировать битву(/get_response: название)')

@dp.message_handler(commands='get_battle')
async def func_start(message: types.Message):
    text = message.get_args()
    print(text)
    response_battle = await get_battle(text)
    await message.answer(response_battle)

@dp.message_handler(commands='get_dnd')
async def func_start(message: types.Message):
    text = message.get_args()
    print(text)
    response_dnd = await get_dnd(text)
    await message.answer(response_dnd)

@dp.message_handler(commands='general_img')
async def func_start(message: types.Message):
    text = message.get_args()
    response_img = await get_response(message.text)
    await message.reply('Идет генерация, подождите')
    try:
        image_data = general_img(response_img)
        await message.reply_photo(photo=image_data)
    except Exception as e:
        await message.reply(f'Произошла ошибка {e}')

@dp.message_handler(commands='get_response')
async def func_start(message: types.Message):
    text = message.get_args()
    response_text = await get_response(message.text)
    print(response_text)
    await message.reply(f"Промпт: {response_text}")

#@dp.message_handler()
#async def hendle_message(message: types.Message):
#   response_text = await get_response(message.text)
#    print(response_text)
#    await message.reply('Идет генерация, подождите')
#    try:
#        image_data = general_img(response_text)
#        await message.reply_photo(photo=image_data)
#    except Exception as e:
#        await message.reply(f'Произошла ошибка {e}')


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)