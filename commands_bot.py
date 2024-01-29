import discord
from discord.ext import commands
import config  # Import the configuration file

# Create an instance of commands.Bot
bot = commands.Bot(command_prefix='!')

# Initialize a dictionary to store ticket information
bot.tickets = {}

# Initialize a dictionary to store the message IDs associated with dropdowns
bot.dropdown_message_ids = {}

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Your setup_crypto_channel function (from the previous response) here

# Your on_select_option function (from the previous response) here

# Run the bot with your token from config.py
bot.run(config.DISCORD_TOKEN)
