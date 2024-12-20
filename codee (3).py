


from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove


from teext import *
from buttonss import *
from commandss import *
from InlineButtonss import *



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


logging.basicConfig(level=logging.INFO)  
bot = Bot(token="TOCKEN")  
dp = Dispatcher()  





@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            types.KeyboardButton(text="Первая помощь"),
            types.KeyboardButton(text="test229"),
            types.KeyboardButton(text="test230"),
            # types.KeyboardButton(text="start"),
            types.KeyboardButton(text="test"),
        ], 
    ] 
    keyboard = types.ReplyKeyboardMarkup( 
        keyboard=kb, 
        resize_keyboard=True, 
        input_field_placeholder="Текст вместо 'Massage'" 
    ) 
    await message.answer("Опции кнопок клавиатуры?", reply_markup=keyboard) 



@dp.message(F.text.lower() == "первая помощь") 
async def cmd_first(message: Message, state: FSMContext):
    await message.answer(
        text="Ответ в формате текста",
        reply_markup=first_aid()
    )



# @dp.message(F.text.lower() == "первая помощь") 
# async def first_aid(message: types.Message):
#     builder = InlineKeyboardBuilder() 
#     builder.row( 
#         types.InlineKeyboardButton(text="Ушиб", callback_data="A1" 
#         ), 
#         types.InlineKeyboardButton(text="Порез", callback_data="A2"), 
#         ) 

#     builder.row( 
#         types.InlineKeyboardButton(text="Ссадины", callback_data="B1"), 
#         types.InlineKeyboardButton(text="Занозы", callback_data="B2"), 
#     ) 

#     builder.row( 
#         types.InlineKeyboardButton(text="Синяки", callback_data="C1"), 
#         types.InlineKeyboardButton(text="Рваные раны", callback_data="C2"),

#     ) 
#     builder.row(
#         types.InlineKeyboardButton(text="Укусы", callback_data="D1"),
#         types.InlineKeyboardButton(text="Прыщи", callback_data="D2"),
#     )
#     await message.answer( 
#         "Ответ в формате Текста:", 
#         reply_markup=builder.as_markup() 
#     ) 





@dp.callback_query(F.data == "A1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(A1)) 
    
        

@dp.callback_query(F.data == "A2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(A2)) 

@dp.callback_query(F.data == "B1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(B1)) 

@dp.callback_query(F.data == "B2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(B2)) 

@dp.callback_query(F.data == "C1") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(C1)) 

@dp.callback_query(F.data == "C2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(C2)) 

@dp.callback_query(F.data == "D1")
async def send_random_value(callback: types.CallbackQuery):  
    await callback.message.answer(str(D1)) 

@dp.callback_query(F.data == "D2") 
async def send_random_value(callback: types.CallbackQuery): 
    await callback.message.answer(str(D2)) 


































async def main():  
    await dp.start_polling(bot) 
    

if __name__ == "__main__":  
    asyncio.run(main())








