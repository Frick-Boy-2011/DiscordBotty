# -*- coding: utf-8 -*-
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from datetime import date
from datetime import time
from datetime import datetime

Donald = ["Dab Donald Dab!","Bitch Dab!","Dab Her Right In The Pussy!", "Dab her by the pussy!","Grab her by the Dabby!" ,"A Small Loan Of A Million Dabs!","Dab On The Fake News!","Thanks Ob-DAB-ma!","Dab the Wall!","Dab the Swamp!","Make DAB-merica Great Again!","Make America DAB Again!", "Make DAB-merica DAB Again"]
JoJoIMG = ["JoJo1.jpg","JoJo2.jpg","JoJo3.jpg","JoJo4.png"]
DIOIMG = ["DIO1.png","DIO2.jpg"]
Client = discord.Client()
client = commands.Bot(command_prefix = "//")
@client.event()
async def on_ready():
    print(">Logged in as:")
    print(">"+client.user.name)
    print(">"+client.user.id)
    print(">Bot is primed")
    
@client.command()
async def on_message(message):
    if message.content == "fuck you":
        await client.send_message(message.channel, "No, Fuck you!")

    if message.content.startswith("//DabDon"):
        r = random.randint(0,12)
        d = Donald[r]
        await client.send_message(message.channel, d)
        await client.send_file(message.channel, 'Images sources/DonDab.jpg')
        print (">Donald Dabs!")
    if message.content.startswith("//ElecDon"):
        
        await client.send_file(message.channel, 'Images sources/ElecTrump.gif')
        print (">Donald Electrocutes")
        
    if message.content.startswith("//DisbeDon"):
        await client.send_file(message.channel, 'Images sources/DisTrump.gif')
        print(">Donald is in Disbelif!")
        
    if message.content.startswith("//DrinkDon"):
        await client.send_file(message.channel, 'Images sources/Drink.png')
        print(">Donald is Drinking!")
        
    if message.content.startswith("//RubioDon"):
        await client.send_file(message.channel, 'Images sources/Rubio.gif')
        print(">Donald is Rubio!")
        
    if message.content.startswith("//Baby"):
        send = message.content.split("-")
        pSend = send[1]
        Proc = pSend
        await client.send_message(message.channel, 'WAAH *'+Proc+'* IM A BABY.')

    if message.content.startswith("//JoJo"):
        send = message.content.split(" ")
        pSend = []
        c = 0
        for item in send:
            if c > 0:
                pSend.append(item)
                c += 1
            else:
                c += 1
        Proc = " ".join(pSend)
        Proc = "*ゴ ゴ ゴ " + Proc +" ゴ ゴ ゴ*"
        if "DIO" in Proc or "Dio" in Proc or "dio" in Proc:
            r = random.randint(0,1)
            d = DIOIMG[r]
            await client.send_file(message.channel, "Images sources/"+d)
            await client.send_message(message.channel, Proc)
        else:
            r = random.randint(0,3)
            j = JoJoIMG[r]
            await client.send_file(message.channel, "Images sources/"+j)
            await client.send_message(message.channel, Proc)
        
            
    if message.content.startswith("//Help"):
        await client.send_message(message.channel, 'Commands: //DabDon, //ElecDon, //DisbeDon, //RubioDon, //Baby, //JoJo')
        print(">Help Given")
    
client.run("NDI0MTU3NzY2OTA3ODU0ODQ4.DY06lw.I4KKHrQjrHBQJY8l9xBWZCrXADc")

