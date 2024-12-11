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
bot = Bot(token="TOKEN")  
dp = Dispatcher()  





@dp.message(Command("start")) 
async def cmd_start(message: types.Message): 
    kb = [ 
        [ 
            
            types.KeyboardButton(text="test228"),
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



@dp.message(F.text.lower() == "test") 
async def cmd_special_buttons(message: types.Message): 
    builder = ReplyKeyboardBuilder() 
    builder.row( 
        types.KeyboardButton(text="Форум"), 
        types.KeyboardButton(text="Форум2"), 
        types.KeyboardButton(text="Форум3"), 
        types.KeyboardButton(text="Форум4"), 
        types.KeyboardButton(text="Форум5"), 
        
    ) 

    builder.row( 
        types.KeyboardButton( 
            text="Назад") 
    ) 
 
    await message.answer( 
        "Выберите действие:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    ) 
 
@dp.message(F.text.lower() == "назад") 
async def with_puree(message: types.Message): 
    kb = [ 
        [ 
            types.KeyboardButton(text="test228"),
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
    await message.reply("Мы снова здесь", reply_markup=keyboard) 




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


# @dp.message(F.text.lower() == "start") 
# async def tic_tac_toe(message: types.Message): 
#     kb = [ 
#         [ 
            
#             types.KeyboardButton(text="test228"),
#             types.KeyboardButton(text="test229"),
#             types.KeyboardButton(text="test230"),
#             types.KeyboardButton(text="start"),
#             types.KeyboardButton(text="спецкнопки"),
#         ], 
#     ] 
#     keyboard = types.ReplyKeyboardMarkup( 
#         keyboard=kb, 
#         resize_keyboard=True, 
#         input_field_placeholder="Текст вместо 'Massage'" 
#     ) 
#     await message.reply("Мы снова здесь", reply_markup=keyboard) 
#     await message.answer("Опции кнопок клавиатуры?", reply_markup=keyboard) 



# @dp.message(F.text.lower() == "назад") 
# async def with_puree(message: types.Message): 
#     kb = [ 
#         [ 
            
#             types.KeyboardButton(text="test228"),
#             types.KeyboardButton(text="test229"),
#             types.KeyboardButton(text="test230"),
#             # types.KeyboardButton(text="start"),
#             types.KeyboardButton(text="test"),
            
            
#         ],  
#         ], 
    
#     keyboard = types.ReplyKeyboardMarkup( 
#         keyboard=kb, 
#         resize_keyboard=True, 
#         input_field_placeholder="Текст вместо 'Massage'" 
#     ) 
#     await message.reply("Мы снова здесь", reply_markup=keyboard) 

#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF




# @dp.message(F.text.lower() == "test") 
# async def cmd_test(message: types.Message): 
#     builder = ReplyKeyboardBuilder() 
#     builder.row( 
#         types.KeyboardButton(text="Запросить геолокацию", request_location=True), 
#         types.KeyboardButton(text="Запросить контакт", request_contact=True) 
#     ) 


#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА
#РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА #РАЗДЕЛ ТЕСТА

@dp.message(F.text.lower() == "test228") 
async def tic_tac_toe(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton( 
            text="A1",  
            callback_data="A1", 
            url = "https://misis.ru" 
        ), 
        types.InlineKeyboardButton( 
            text="A2",  
            callback_data="A2",
            url = "https://ya.ru/"
            
        ), 
        types.InlineKeyboardButton(text="A3", callback_data="A3" ),
        types.InlineKeyboardButton(text="A4", callback_data="A4")
        ) 
            
    

    

    builder.row( 
        types.InlineKeyboardButton(text="B1", callback_data="B1"), 
        types.InlineKeyboardButton(text="B2", callback_data="B2"), 
        types.InlineKeyboardButton(text="B3", callback_data="B3"),
        types.InlineKeyboardButton(text="B4", callback_data="B4")
    ) 

    builder.row( 
        types.InlineKeyboardButton(text="C1", callback_data="C1"), 
        types.InlineKeyboardButton(text="C2", callback_data="C2"), 
        types.InlineKeyboardButton(text="C3", callback_data="C3"),
        types.InlineKeyboardButton(text="C4", callback_data="C4")
    ) 
    builder.row(
        types.InlineKeyboardButton(text="D1", callback_data="D1"),
        types.InlineKeyboardButton(text="D2", callback_data="D2"),
        types.InlineKeyboardButton(text="D3", callback_data="D3"),
        types.InlineKeyboardButton(text="D4", callback_data="D4")
    )
    
    await message.answer( 
        "Soveti:", 
        reply_markup=builder.as_markup() 
    ) 



@dp.message(F.text.lower() == "test229") 
async def tic_tac_toe(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton( 
            text="A1",  
            callback_data="A1", 
            url = "https://misis.ru" 
        ), 
        types.InlineKeyboardButton( 
            text="A2",  
            callback_data="A2",
            url = "https://ya.ru/"
            
        ), 
        types.InlineKeyboardButton(text="A3", callback_data="A3" ),
        types.InlineKeyboardButton(text="A4", callback_data="A4")
        ) 
            
    

    

    builder.row( 
        types.InlineKeyboardButton(text="B1", callback_data="B1"), 
        types.InlineKeyboardButton(text="B2", callback_data="B2"), 
        types.InlineKeyboardButton(text="B3", callback_data="B3"),
        types.InlineKeyboardButton(text="B4", callback_data="B4")
    ) 

    builder.row( 
        types.InlineKeyboardButton(text="C1", callback_data="C1"), 
        types.InlineKeyboardButton(text="C2", callback_data="C2"), 
        types.InlineKeyboardButton(text="C3", callback_data="C3"),
        types.InlineKeyboardButton(text="C4", callback_data="C4")
    ) 
    builder.row(
        types.InlineKeyboardButton(text="D1", callback_data="D1"),
        types.InlineKeyboardButton(text="D2", callback_data="D2"),
        types.InlineKeyboardButton(text="D3", callback_data="D3"),
        types.InlineKeyboardButton(text="D4", callback_data="D4")
    )
    
    await message.answer( 
        "Soveti2:", 
        reply_markup=builder.as_markup() 
    ) 




@dp.message(F.text.lower() == "test230") 
async def tic_tac_toe(message: types.Message): 
    builder = InlineKeyboardBuilder() 
    builder.row( 
        types.InlineKeyboardButton( 
            text="A1",  
            callback_data="A1", 
            url = "https://misis.ru" 
        ), 
        types.InlineKeyboardButton( 
            text="A2",  
            callback_data="A2",
            url = "https://ya.ru/"
            
        ), 
        types.InlineKeyboardButton(text="A3", callback_data="A3" ),
        types.InlineKeyboardButton(text="A4", callback_data="A4")
        ) 
            
    

    

    builder.row( 
        types.InlineKeyboardButton(text="B1", callback_data="B1"), 
        types.InlineKeyboardButton(text="B2", callback_data="B2"), 
        types.InlineKeyboardButton(text="B3", callback_data="B3"),
        types.InlineKeyboardButton(text="B4", callback_data="B4")
    ) 

    builder.row( 
        types.InlineKeyboardButton(text="C1", callback_data="C1"), 
        types.InlineKeyboardButton(text="C2", callback_data="C2"), 
        types.InlineKeyboardButton(text="C3", callback_data="C3"),
        types.InlineKeyboardButton(text="C4", callback_data="C4")
    ) 
    builder.row(
        types.InlineKeyboardButton(text="D1", callback_data="D1"),
        types.InlineKeyboardButton(text="D2", callback_data="D2"),
        types.InlineKeyboardButton(text="D3", callback_data="D3"),
        types.InlineKeyboardButton(text="D4", callback_data="D4")
    )
    
    await message.answer( 
        "Soveti3:", 
        reply_markup=builder.as_markup() 
    ) 







async def main():  
    await dp.start_polling(bot)  



async def main():  
    await dp.start_polling(bot)  




@dp.message(Command("name"))  
async def cmd_name(message: types.Message):  
    await message.answer("My name is test!")  



@dp.message(Command('help')) 
async def cmd_help(message: types.Message): 
    await message.answer("Список команд:\n/help - список команд\n/start - запуск бота\n/ban - блокировка пользователя\n/mute - блокировка чата пользователю\n/kick - исключить пользователя") 


@dp.message(Command('')) 
async def cmd_(message: types.Message): 
    await message.answer("") 



if __name__ == "__main__":  
    asyncio.run(main())