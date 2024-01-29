import discord
from discord.ext import commands
from crypto_channel import setup_crypto_channel
import config  # Import the configuration file

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready')
    await bot.tree.sync()
    setup_crypto_channel(bot)

@bot.event
async def on_message(msg:discord.Message):
    content=msg.content
    print(content)
    if content.startswith('!'):
        await bot.process_commands(msg)
    if content=="hello":
        await msg.channel.send("Hi!")

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!', ephemeral=True)    

@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello!', ephemeral=True)

bot.run(config.DISCORD_TOKEN)
