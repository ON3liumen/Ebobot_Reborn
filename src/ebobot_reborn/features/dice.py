#import
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import random


router = Router()

#wait for command /dice
@router.message(Command("dice"))
async def roll(message: Message):
    #roll a dice
    dice_roll = random.randint(1, 6)
    await message.answer(f"you rolled: {dice_roll}")
