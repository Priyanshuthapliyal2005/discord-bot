import discord
from discord.ext import commands
from common import MiddlemanBot

class CryptoChannel:
    @classmethod
    def setup_crypto_channel(cls, bot):
        @bot.command(name='crypto_channel')
        async def crypto_channel(ctx):
            options = [
                "Bitcoin",
                "Ethereum",
                "Litecoin",
                "Solana",
            ]

            # Display options in a dropdown
            dropdown = discord.ui.Select(
                placeholder="Select a cryptocurrency",
                options=[discord.SelectOption(label=option, value=option.lower()) for option in options]
            )


            # Send a message with the dropdown
            message = await ctx.send("Select a cryptocurrency:", view=discord.ui.View().add_item(dropdown))

            # Store the message ID for reference in on_select_option
            bot.dropdown_message_ids[message.id] = ctx.author.id

        @bot.event
        async def on_select_option(interaction: discord.Interaction, select_menu: discord.ui.Select):
            # Retrieve the user who initiated the command
            user_id = bot.dropdown_message_ids.get(interaction.message.id)
            user = interaction.guild.get_member(user_id)

            # Handle the selected option
            await interaction.response.send_message(f"You selected: {select_menu.values[0]}", ephemeral=True)

            # Provide instructions on how to create a ticket using Ticket Tool Bot
            await interaction.followup.send(f"To create a ticket related to {select_menu.values[0]} using Ticket Tool Bot, use the command: `$new {select_menu.values[0]}`")

# You can add more classes and functionalities as needed