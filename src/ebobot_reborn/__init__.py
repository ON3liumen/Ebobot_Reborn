#dependencies
import asyncio
from aiogram import Bot, Dispatcher
import yaml
#from .features import example


#main function
def main():
    asyncio.run(run())


#run bot

async def run():
    bot = Bot(token="......")
    dp = Dispatcher()

#features

#dp.include_router(example.router)





#keep polling
    await dp.start_polling(bot)

