# bot.py - Import common functionality
import discord
from discord.ext import commands
from common import bot
from crypto_channel import setup_crypto_channel
import config  # Import the configuration file

@bot.event
async def on_ready():
    print('Bot is ready')
    await bot.tree.sync()
    setup_crypto_channel(bot)

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!', ephemeral=True)    

@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello!', ephemeral=True)

bot.run(config.DISCORD_TOKEN)
