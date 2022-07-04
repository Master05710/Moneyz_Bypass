#Source Code Для обхода рекламы (накручивать) moneyz.fun.
#Создателем является GGCheater


import logging
from dateutil import parser
import sqlite3
import os
import sys
import requests
import time
import string
import random
import asyncio
from aiogram import Bot,Dispatcher, executor, types
import threading
from threading import Thread
import re
from datetime import datetime, timedelta
from asyncio import new_event_loop, set_event_loop
import queue
from queue import Queue
import aiohttp
import asyncio
from time import sleep
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import Throttled
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
PREFIX = "/,!,?"

bot = Bot(
    token='   ')
dp = Dispatcher(bot=bot,storage=storage)

async def try_or(fn, df):
    try:
        return await fn()
    except Exception as err:
        print(14)
        print(err)
        return df
    
def try_or(fn, df):
    try:
        return fn()
    except Exception as err:
        print(14)
        print(err)
        return df            
            
async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не гоняй.")            
            
            
async def Bypass(click):
    proxies = {'http': ''} #резидент прокси (можно и простой http)
    s = requests.session()
    s.proxies.update(proxies)
    param = {'click_link_key': f'{click}'}
    print(param)
    try:
        return s.post(f"https://moneyz.fun/action.php",  headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}, data=param).json()
    except:
       time.sleep(2)

@dp.message_handler(commands=['start'], commands_prefix=PREFIX)
@dp.throttled(anti_flood,rate=3)
async def start_checker(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["💻Bypass Moneyz💻"]
    keyboard.add(*buttons)
    await message.answer("🤖 Это бот созданным GGCheater'om для обхода рекламы в сервисе Money'z.", reply_markup=keyboard) 
    
@dp.message_handler(lambda message: message.text == "💻Bypass Moneyz💻")
@dp.throttled(anti_flood,rate=3)
async def without_puree(message: types.Message):
    await message.answer("/bypass ID")
    await bot.send_photo(message.from_user.id, 'https://i.postimg.cc/V5PPBL28/Screenshot-20220609-112740-1.png')

@dp.message_handler(commands="bypass")
@dp.throttled(anti_flood,rate=17)
async def cc(message: types.Message):
    bbs = message.text[len('/bypass '):]
    user = message.from_user.username
    chatikid = message.from_user.id
    bbs = message.text[len('/bypass'):]
    user = message.from_user.username
    bcs = bbs.split(sep=None, maxsplit=999)
    user = message.from_user.username
    for id in bbs:
        bcs = id.capitalize()
        asd = re.findall("(.)(......)", bbs)
    print(asd[0][1])
    if asd == []:
            await message.reply("используй так: /bypass ID")
            return
    time.sleep(1)
    if not len(str(asd[0][1])) == 6:
            await message.reply("Err...")
            return
    try:
        bind = await Bypass(asd[0][1])
        print(bind)
        await message.reply(f"📖 EASY BYPASS YOUR LINK (by GGCheater): " + bind["link_full_val"])
    except KeyError as e:
            await messageFirst.edit_text("Erroooorrr!!")
    except:
            print('бляяя')
     
if __name__ == '__main__':
    set_event_loop(new_event_loop())
    executor.start_polling(dp, skip_updates=True)
    
#Fuck Moneyz🤡👎
