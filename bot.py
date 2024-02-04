import discord
# from discord.ext import commands
# from common import MiddlemanBot
# from crypto_channel import CryptoChannel

# import config  # Import the configuration file

# bot = MiddlemanBot(command_prefix='!', intents=discord.Intents.all())

# @bot.event
# async def on_ready():
#     print('Bot is ready')
#     await bot.tree.sync()
#     CryptoChannel.setup_crypto_channel(bot)

# @bot.tree.command()
# async def ping(interaction: discord.Interaction):
#     await interaction.response.send_message('Pong!', ephemeral=True)

# @bot.tree.command()
# async def hello(interaction: discord.Interaction):
#     await interaction.response.send_message('Hello!', ephemeral=True)

# class MiddlemanSetup(discord.ui.View):
#     def __init__(self, interaction: discord.Interaction, crypto_confirmation_message: discord.Message):
#         super().__init__()
#         self.crypto_confirm_view = CryptoConfirmView(self, crypto_confirmation_message)

#     async def on_timeout(self):
#         # This method will be called if the view times out (no interaction)
#         self.clear_items()

#     async def interaction_check(self, interaction: discord.Interaction):
#         # Additional check for the interaction
#         return interaction.user.id == self.interaction.user.id

#     async def update_panel(self):
#         # This method updates the panel based on the selected role
#         self.clear_items()

#         if self.role == 'Sending':
#             self.add_item(discord.ui.Button(label=f'Sending - {self.interaction.user.name}', style=discord.ButtonStyle.green, disabled=True))
#             self.add_item(discord.ui.Button(label='Receiving', style=discord.ButtonStyle.red, custom_id='receiving_button'))
#             self.add_item(discord.ui.Button(label='Reset', style=discord.ButtonStyle.grey, custom_id='reset_button'))
#         elif self.role == 'Receiving':
#             self.add_item(discord.ui.Button(label='Sending', style=discord.ButtonStyle.blurple, custom_id='sending_button'))
#             self.add_item(discord.ui.Button(label=f'Receiving - {self.interaction.user.name}', style=discord.ButtonStyle.red, disabled=True))
#             self.add_item(discord.ui.Button(label='Reset', style=discord.ButtonStyle.grey, custom_id='reset_button'))
#         else:
#             self.add_item(discord.ui.Button(label='Sending', style=discord.ButtonStyle.green, custom_id='sending_button'))
#             self.add_item(discord.ui.Button(label='Receiving', style=discord.ButtonStyle.blurple, custom_id='receiving_button'))
#             self.add_item(discord.ui.Button(label='Reset', style=discord.ButtonStyle.grey, custom_id='reset_button'))

#         if self.message:
#             await self.crypto_confirm_view.message.edit(view=self.crypto_confirm_view)

#     async def sending(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.role = 'Sending'
#         self.sending_user = interaction.user
#         await interaction.response.defer()
#         await self.update_panel()

#     async def receiving(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.role = 'Receiving'
#         self.receiving_user = interaction.user
#         await interaction.response.defer()
#         await self.update_panel()

#     async def reset(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.role = None
#         self.sending_user = interaction.user
#         self.receiving_user = interaction.user
#         await interaction.response.defer()
#         await self.update_panel()

# class Crypto(discord.ui.View):
#     def __init__(self, interaction):
#         super().__init__(timeout=None)  # Disable timeout
#         self.value = None
#         self.interaction = interaction

#     @discord.ui.button(label='Bitcoin', style=discord.ButtonStyle.green, custom_id='bitcoin_button')
#     async def bitcoin(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.value = 'Bitcoin'
#         await interaction.response.defer()
#         self.stop()

#     @discord.ui.button(label='Ethereum', style=discord.ButtonStyle.gray ,custom_id='ethereum_button')
#     async def ethereum(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.value = 'Ethereum'
#         await interaction.response.defer()
#         self.stop()

#     @discord.ui.button(label='Litecoin', style=discord.ButtonStyle.blurple, custom_id='litecoin_button')
#     async def litecoin(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.value = 'Litecoin'
#         await interaction.response.defer()
#         self.stop()

#     @discord.ui.button(label='Solana', style=discord.ButtonStyle.red, custom_id='solana_button')
#     async def solana(self, interaction: discord.Interaction, button: discord.ui.Button):
#         self.value = 'Solana'
#         await interaction.response.defer()
#         self.stop()

# class CryptoConfirmView(discord.ui.View):
#     def __init__(self, middleman_setup: MiddlemanSetup, crypto_confirmation_message: discord.Message):
#         super().__init__()
#         self.middleman_setup = middleman_setup
#         self.crypto_confirmation_message = crypto_confirmation_message

#     @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
#     async def confirm_crypto_setup(self, button: discord.ui.Button, interaction: discord.Interaction):
#         # Your existing code here
#         self.message = await interaction.response.send_message("Your crypto setup has been confirmed.", ephemeral=True)
# @bot.tree.command()
# async def middleman_setup(interaction: discord.Interaction):
#     await interaction.response.send_message(
#         'Cryptocurrency Middleman System\n'
#         'Welcome to our automated cryptocurrency Middleman system!\n'
#         'Your cryptocurrency will be stored securely until the deal is completed.\n'
#         'The system ensures the security of both users by securely storing the funds until the deal is complete and confirmed by both parties.\n'
#         ':Alert: Our bot will NEVER DM you! Please report any suspicious DMs to Staff.\n'
#         'Role Selection\n'
#         'Tag the user you want to deal. (e.g., @user)',
#     )

#     def check_tagged_user(message: discord.Message):
#         return (
#             message.author == interaction.user and 
#             (message.mentions or any(word.startswith('@') for word in message.content.split()))
#         )

#     tagged_user_message = await bot.wait_for('message', check=check_tagged_user)
#     middleman_user = tagged_user_message.mentions[0] if tagged_user_message.mentions else None

#     if not middleman_user:
#         # Extract user from the mention format (@username)
#         mention_parts = tagged_user_message.content.split()
#         for part in mention_parts:
#             if part.startswith('@'):
#                 user_name = part[1:]
#                 members = [member for member in interaction.guild.members if member.name == user_name]
#                 if members:
#                     middleman_user = members[0]
#                     break

#     if not middleman_user:
#         await interaction.followup.send('Invalid user mentioned. Please try again.')
#         return

#     tagged_user_response = await interaction.followup.send(f'You tagged {middleman_user}')
#     view = Crypto(interaction)
#     crypto_confirmation_message = await interaction.followup.send(
#         'Please confirm your crypto before proceeding.',
#         view=view, ephemeral=True
#     )
#     await view.wait()

#     selected_crypto = view.value

#     if not selected_crypto:
#         await interaction.followup.send('No cryptocurrency has been selected. Please try again.', ephemeral=True)
#         return

#     view = MiddlemanSetup(interaction, crypto_confirmation_message)
#     middleman_setup_message = await interaction.followup.send(
#         'Please select one of the following buttons that corresponds to your role in this deal. Once selected, both users must confirm to proceed.',
#         view=view, ephemeral=True
#     )
#     view.message = {
#     'tagged_user': tagged_user_response,
#     'crypto_confirmation': crypto_confirmation_message,
#     'middleman_setup': middleman_setup_message,
#     'crypto_confirm_view': view,
#     }
    
#     await view.update_panel()
#     await view.wait()

#     # Use the selected_crypto variable to proceed with the transaction
#     await interaction.followup.send(f'You selected: {selected_crypto}', ephemeral=True)

# bot.run(config.DISCORD_TOKEN)
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

@bot.command()
async def tnc(ctx):
    await ctx.send("Terms of Service\n\n"
                   "By using this service, you accept the Discord ToS, and the following terms\n\n"
                   "User Liability\n"
                   "While using this service, it is your duty to ensure that you are reading and acknowledging provided prompts. "
                   "User errors are not insured, and will result in the loss of your cryptocurrency/valuables.\n\n"
                   "Service Safety\n"
                   "If we perceive something as suspicious, or against the ToS, we have the authority to decline your request. "
                   "Any deals involving gift cards, accounts, or unfamiliar content are prohibited.\n\n"
                   "Account Security\n"
                   "While using this service, it is your responsibility to ensure the safety of your account. "
                   "If your account is compromised, we are not liable for any losses.\n\n"
                   "User Guarantee\n"
                   "By using this service, you are guaranteed the safety of your funds. "
                   "All funds lost in our possession following a bot error will be compensated 1:1. User errors will not be compensated."
                   , ephemeral=True)
    
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
