'''
Paul Woody
Feb 2019
Github.com/pawoody
Simple bot that inverts what users say and randomly replies from a list of pre-made messages.
'''

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio
import random
import string

'''
Define global variables we'll use to irritate our friends. 
Create list of phrases to be called on later assigned to 'retorts'. 
Create variable to insert spacing in bot replies.
'''
bot = commands.Bot(command_prefix='*')
q = ()
wacky = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
retorts = [f"Name's Big Chungus but you can call me Jonny Jackson.", f"My real name is actually {bot.user} but no one calls me that.", "Wanna hear the World's most annoying sound?", f"Hey! HEY! HEEEYYY! \n\n\n\n\n\n\n\n\n\n Hi again. \n\n\n\n\n\n  I'm still here!", f"Hiii! \n\n\n My favorite way to pronoune 'cracker' is: {wacky}"]

'''
Print a little info about our bot to the console for reference.
'''
@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')
  #await message.channel.send
  #await bot.send_message(message.channel, message.content)

'''
Forces bot to prioritize commands before automatically parsing events.
'''
@bot.event
async def on_message(message):
  await bot.process_commands(message)

'''
Checks to see if the author of any new printed text is a user other than the bot.  If the text is not from the bot, the bot will repeat the user's text backwards and taunts them a bit.
'''
@bot.event
async def on_message(message):
  if message.author != bot.user:      
    await bot.send_message(message.channel, message.content[::-1])
    q = ()
    await bot.send_message(message.channel, f"Do you enjoy it when I do that, {message.author}?")
  await bot.process_commands(message)

'''
Creates the greet command.  Bot will still repeat user's message backwards, but will then print the message below followed by a random element from the 'retorts' list.
'''
@bot.command()
async def greet():
#return random message
  await bot.say(f"I am a crappy and annoying bot, and no one will ever love me. :( {random.choice(retorts[0:6])}")
    
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)











'''
UNFINISHED CODE:
#Greets Users when logging on
@client.event
async def on_ready():
    print(start)
    await ctx.message.channel.send
'''

'''
@bot.event
async def on_message(message):
  if message.content.startswith('!count'):
    counter = 0
    tmp = await bot.send_message(message.channel, 'Please wait...')
  async for log in bot.logs_from(message.channel, limit=100):
    if log.author == message.author:
      counter += 1
      return counter
'''