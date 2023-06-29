import dotenv

dotenv.load_dotenv()

import os
import random
from datetime import datetime as dt 

import json

config = json.load(open('data.json', 'r'))

import logging
from logging.config import dictConfig

dictConfig({
    "version": 1,
    "disabled_existing_loggers": False,
    
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/info.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    
    "loggers": {
        "bot": {
            "handlers": ['console'],
            "level": "INFO",
            "propagate": False
        },
        
        "discord": {
            "handlers": ['console2', 'file'],
            "level": "INFO",
            "propagate": False
        }
    }
})

logger = logging.getLogger('bot')

import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(
    command_prefix = config['prefix'],
    case_insensitive = True,
    intents = intents)

# Ready Message
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='727 WYSI'))
    # loadExt()
    logging.info(f"Nen is online as {client.user} (ID: {client.user.id})")

@client.event
async def on_command_error(ctx, error):
    logging.error(f"{type(error).__name__}: {error}")

# Defualt Message
@client.command(brief = 'Default Command')
async def nen(ctx):
    emojis = ['🐖', '🐕‍🦺', '🦙', '🐅', '🐍', '🐑', '🐧', '🐒']
    await ctx.send('Searching for senpai\'s codes! ' + random.choice(emojis))

client.run(str(os.getenv('DISCORD_BOT_TOKEN')), root_logger = True)