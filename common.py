# common.py - Define common functionality here
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize a dictionary to store ticket information
bot.tickets = {}

# Initialize a dictionary to store the message IDs associated with dropdowns
bot.dropdown_message_ids = {}
