# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 00:21:34 2021

@author: ACER
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "1919083325:AAExNBa7jAEAdxj9bOohC0av7rytG7CIdjg" #<-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    tanish="Bismillahir Rohmanir Rohim Alhamdulillah \U0001F917" 
    tanish+="\nXush kelibsiz!"
    tanish+="\nMatn kiriting "
    bot.reply_to(message, tanish)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    #if msg.isascii():
     #   javob=to_cyrillic(msg)
    #else:
    #    javob=to_latin(msg)
    bot.reply_to(message, javob(msg))
    
    

bot.polling()

#
# manzili tme:@OLLIT_DEV_bot  yoki {   Lotin ∞ Крилл  }


#matn=input("matn kiriting: ")
#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
