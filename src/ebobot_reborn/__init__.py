#dependencies
import asyncio
from aiogram import Bot, Dispatcher
import yaml
from .features import dice


# load config.yaml
def load_config(path="config.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)

#main function
def main():
    asyncio.run(run())


#run bot

async def run():
    config = load_config()

    bot = Bot(token=config["bot"]["token"])
    dp = Dispatcher()
    dp["config"] = config
    
#features

    dp.include_router(dice.router)





#keep polling
    await dp.start_polling(bot)

