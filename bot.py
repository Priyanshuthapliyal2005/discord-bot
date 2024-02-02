
import discord
from discord.ext import commands
from common import MiddlemanBot
from crypto_channel import CryptoChannel

import config  # Import the configuration file

bot = MiddlemanBot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready')
    await bot.tree.sync()
    CryptoChannel.setup_crypto_channel(bot)

@bot.tree.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!', ephemeral=True)

@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello!', ephemeral=True)

class MiddlemanSetup(discord.ui.View):
    def __init__(self, interaction):
        super().__init__(timeout=None)  # Disable timeout
        self.value = None
        self.interaction = interaction

    @discord.ui.button(label='Sending', style=discord.ButtonStyle.green, custom_id='sending_button')
    async def sending(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Sending'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='Receiving', style=discord.ButtonStyle.red, custom_id='receiving_button')
    async def receiving(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Receiving'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='Reset', style=discord.ButtonStyle.red, custom_id='reset_button')
    async def reset(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Reset'
        await interaction.response.defer()
        self.stop()

class Crypto(discord.ui.View):
    def __init__(self, interaction):
        super().__init__(timeout=None)  # Disable timeout
        self.value = None
        self.interaction = interaction

    @discord.ui.button(label='Bitcoin', style=discord.ButtonStyle.green, custom_id='bitcoin_button')
    async def bitcoin(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Bitcoin'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='Ethereum', style=discord.ButtonStyle.red, custom_id='ethereum_button')
    async def ethereum(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Ethereum'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='Litecoin', style=discord.ButtonStyle.red, custom_id='litecoin_button')
    async def litecoin(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Litecoin'
        await interaction.response.defer()
        self.stop()

    @discord.ui.button(label='Solana', style=discord.ButtonStyle.red, custom_id='solana_button')
    async def solana(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 'Solana'
        await interaction.response.defer()
        self.stop()

@bot.tree.command()
async def middleman_setup(interaction: discord.Interaction):
    await interaction.response.send_message(
        'Cryptocurrency Middleman System\n'
        'Welcome to our automated cryptocurrency Middleman system!\n'
        'Your cryptocurrency will be stored securely till the deal is completed.\n'
        'The system ensures the security of both users by securely storing the funds until the deal is complete and confirmed by both parties.\n'
        ':Alert: Our bot will NEVER dm you! Please report any suspicious DMs to Staff.\n'
        'Role Selection\n'
        'Tag the user you want to deal. (e.g @user)',
    )

    def check_tagged_user(message: discord.Message):
        return (
            message.author == interaction.user and 
            (message.mentions or any(word.startswith('@') for word in message.content.split()))
        )

    tagged_user_message = await bot.wait_for('message', check=check_tagged_user)
    middleman_user = tagged_user_message.mentions[0] if tagged_user_message.mentions else None

    if not middleman_user:
        # Extract user from the mention format (@username)
        mention_parts = tagged_user_message.content.split()
        for part in mention_parts:
            if part.startswith('@'):
                user_name = part[1:]
                members = [member for member in interaction.guild.members if member.name == user_name]
                if members:
                    middleman_user = members[0]
                    break

    if not middleman_user:
        await interaction.followup.send('Invalid user mentioned. Please try again.')
        return

    await interaction.followup.send(f'You tagged {middleman_user}')
    view= Crypto(interaction)
    await interaction.followup.send(
        'Please Confirm you crypto before preceding.',
        view=view, ephemeral=True
    )
    await view.wait()
    view = MiddlemanSetup(interaction)
    await interaction.followup.send(
        'Please select one of the following buttons that corresponds to your role in this deal. Once selected, both users must confirm to proceed.',
        view=view, ephemeral=True
    )
    await view.wait()
    await interaction.followup.send(f'You selected: {view.value}', ephemeral=True)

bot.run(config.DISCORD_TOKEN)
