import asyncio  
import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.filters.command import Command  
from configs import Config 
from aiogram import F 
from random import randint 
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram.utils.keyboard import InlineKeyboardBuilder 
import sqlite3



import proekt.buttonss



logging.basicConfig(level=logging.INFO)  
bot = Bot(token="TOCKEN")  
dp = Dispatcher()  



@dp.message(Command("start"))



@dp.message(F.text.lower() == "test")




@dp.message(F.text.lower() == "форум")




@dp.message(F.text.lower() == "форум2")


@dp.message(F.text.lower() == "форум3")



@dp.message(F.text.lower() == "форум4")



@dp.message(F.text.lower() == "форум5")


@dp.message(F.text.lower() == "назад")



@dp.message(F.text.lower() == "первая помощь") 


@dp.message(Command("help")) 
async def cmd_start(message: types.Message):
    await message.answer("умный тест хз") 
