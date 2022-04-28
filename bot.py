# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:46:18 2022

@author: pc
"""

from telebot import TeleBot

import requests
bot = TeleBot("5365894244:AAG6hMkEdEZLpr87078XMhfVfZ2ogR3Pbio")



def eth(coin):
    parite="eth"
    try:
        url=f"https://api.fmfw.io/api/3/public/price/rate?from={coin}&to={parite}"
        a=requests.get(url)
        parite=parite.upper()
        coin=coin.upper()
        fiyat=(a.text.split('"')[9])
        return(f"""
{parite}
{coin}:{fiyat}""")
    except:
        return(f"")
    
def usdt(coin):
    parite="usdt"
    try:
        url=f"https://api.fmfw.io/api/3/public/price/rate?from={coin}&to={parite}"
        a=requests.get(url)
        
        fiyat=(a.text.split('"')[9])
        
        parite=parite.upper()
        coin=coin.upper()
        return(f"""
{parite}
{coin}:{fiyat}""")
    except:
        return(f"")
    
    

def btc(coin):
    parite="btc"
    try:
        url=f"https://api.fmfw.io/api/3/public/price/rate?from={coin}&to={parite}"
        a=requests.get(url)
        
        fiyat=(a.text.split('"')[9])
        
        parite=parite.upper()
        coin=coin.upper()
        return(f"""
{parite}
{coin}:{fiyat}""")
    except:
        return(f"")
def bch(coin):
    parite="bch"
    try:
        url=f"https://api.fmfw.io/api/3/public/price/rate?from={coin}&to={parite}"
        a=requests.get(url)
        
        fiyat=(a.text.split('"')[9])
        
        parite=parite.upper()
        coin=coin.upper()
        return(f"""
{parite}
{coin}:{fiyat}""")
    except:
        return(f"")


@bot.message_handler(['fiyat'])
def give(m):
    try:
        print("s")
        giris=m.text
        coin=giris.split(" ")[1]
        metin=(f"""
      {btc(coin)}
      {usdt(coin)}
      {eth(coin)}
      {bch(coin)}
      """)
        bot.reply_to (m,metin)
    except:
        pass
@bot.message_handler(['price'])
def give1(m):
    try:
        print("s")
        giris=m.text
        coin=giris.split(" ")[1]
        metin=(f"""
      {btc(coin)}
      {usdt(coin)}
      {eth(coin)}
      {bch(coin)}
      """)
        bot.reply_to (m,metin)
    except:
        pass

@bot.message_handler(['Price'])
def give1(m):
    try:
        print("s")
        giris=m.text
        coin=giris.split(" ")[1]
        metin=(f"""
      {btc(coin)}
      {usdt(coin)}
      {eth(coin)}
      {bch(coin)}
      """)
        bot.reply_to (m,metin)
    except:
        pass

@bot.message_handler(['Fiyat'])
def give(m):
    try:
        print("s")
        giris=m.text
        coin=giris.split(" ")[1]
        metin=(f"""
      {btc(coin)}
      {usdt(coin)}
      {eth(coin)}
      {bch(coin)}
      """)
        bot.reply_to (m,metin)
    except:
        pass
    
  




    
        
bot.polling()