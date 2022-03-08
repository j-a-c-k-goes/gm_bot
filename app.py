''' system modules '''
import os
import discord
import logging
from dotenv import load_dotenv
import random
''' content modules '''
from emojis import *
from std_greetings import *
from units_of_time import *
from like_as_with import *
from to_begin import *
from emo_ingredients import *
from boondocks_char import *
from punc import *
from global_gm import *
''' function modules '''
from vee_gm import *
from non_us_gm import *
from boondocks_gm import *
from base_gm import *
from time_gm import *
from global_gm import *

''' server/guild setup '''
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
SERVER = os.getenv('TW_SERVER')
live = 'TW_CHANNEL'
test = 'TEST_CHANNEL'
CHANNEL = os.getenv(test) #TW_CHANNEL #TEST_CHANNEL
TEST_CHANNEL = os.getenv('TEST_CHANNEL')
BREAD = '<:br3ad:900045472088084510>'

''' create client instance '''
client = discord.Client()

''' logging setup '''
#logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
#handler = logging.FileHandler(filename='gm_bot.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctimes)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

''' gm bot self messages '''
def gm_bot_self():
    output_a = f'gm_bot™\tbooting from terminal'
    output_b = f'--- going to Trav\'s World Server @ {SERVER}\tworking in {TEST_CHANNEL} ---'
    outputs = [output_a, output_b]
    xyz = random.choice(outputs)
    return xyz

''' bot finished logging in '''
@client.event
async def on_ready():
    gm_bot_to_self = gm_bot_self()
    print(gm_bot_to_self)

@client.event
async def on_typing(channel, user, when):
    message_author = user
    message_channel = channel
    print(user, "started to type in", channel, "on", when)
    
''' when bot receives a message, applies to every message '''
@client.event
async def on_message(message):
    #if message.author == client.user:
    #return
    if message.content.startswith('gm'.lower()):
        await message.reply(f'{boondocks_gm(boondocks_characters)} {BREAD}')
    elif message.content.startswith('gm'.upper()):
        await message.reply(f'{vee_gm(emo_ingredients, like_as_with)}')
    elif message.content.startswith('gm'.title()):
        await message.reply(f'{base_gm(general_emojis, standard_greetings, punctuation, to_begin, like_as_with)}')
    elif message.content.startswith('morning'):
        await message.reply(f'{time_gm(units_of_time, like_as_with, general_emojis, emo_ingredients)}')
    elif message.content.startswith('TOD'):
        await message.reply(f'{global_gm(non_american_gm, general_emojis)}')
    print(f'gm bot sent a reply to {SERVER} in {TEST_CHANNEL}')

''' on disconnect '''
@client.event
async def on_disconnect():
    gm_bot_to_self = gm_bot_self(general_emojis)
    print(f'gm bot is {client.user} from {client.id}, until next time')
''' run bot '''
client.run(TOKEN)
