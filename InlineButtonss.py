
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

dp = Dispatcher()  



@dp.message(F.text.lower() == "форум")
async def forum(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )

    await message.answer( 
        "Ссылки:", 
        reply_markup=builder.as_markup() 
    ) 






@dp.message(F.text.lower() == "форум2")
async def forum(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )

    await message.answer( 
        "Ссылки:", 
        reply_markup=builder.as_markup() 
    ) 







@dp.message(F.text.lower() == "форум3")
async def forum(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )

    await message.answer( 
        "Ссылки:", 
        reply_markup=builder.as_markup() 
    ) 



@dp.message(F.text.lower() == "форум4")
async def forum(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )

    await message.answer( 
        "Ссылки:", 
        reply_markup=builder.as_markup() 
    ) 






@dp.message(F.text.lower() == "форум5")
async def forum(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="A1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="A2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="A3")
        )

    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="B1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="B2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="B3")
        )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="C1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="C2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="C3")
    )
    builder.row( 
        types.InlineKeyboardButton(text="Ссылка1", callback_data="D1"),
        types.InlineKeyboardButton(text="Ссылка2", callback_data="D2" ),
        types.InlineKeyboardButton(text="Ссылка3", callback_data="D3")
    )

    await message.answer( 
        "Ссылки:", 
        reply_markup=builder.as_markup() 
    ) 