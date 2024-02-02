import discord
from discord.ext import commands
from common import bot

def setup_crypto_channel(bot):
    @bot.command(name='crypto_channel')
    async def crypto_channel(ctx):
        # Create an embed with the provided information
        embed = discord.Embed(
            title="Cryptocurrency",
            description="Fees:\nDeals $500+: 0.5%\nDeals under $500: $2\nWarranty 24h+: 1%\nDeals under $50 are FREE",
            color=discord.Color.green()
        )

        # Add a dropdown menu
        dropdown = discord.ui.Select(
            placeholder="Select a cryptocurrency",
            options=[
                discord.SelectOption(label="Bitcoin", value="bitcoin"),
                discord.SelectOption(label="Ethereum", value="ethereum"),
                discord.SelectOption(label="Litecoin", value="litecoin"),
                discord.SelectOption(label="Solana", value="solana"),
            ]
        )

        # Add the dropdown to the embed
        embed.add_field(name="Select Cryptocurrency", value="Press the dropdown below to select & initiate a deal involving either Bitcoin, Ethereum, Litecoin, or Solana.", inline=False)
        
        # Send the embed with the dropdown
        message = await ctx.send(embed=embed, view=discord.ui.View().add_item(dropdown))

        # Store the message ID for reference in on_select_option
        bot.dropdown_message_ids[message.id] = ctx.author.id

    @bot.event
    async def on_select_option(interaction: discord.Interaction, select_menu: discord.Select):
        # Retrieve the user who initiated the command
        user_id = bot.dropdown_message_ids.get(interaction.message.id)
        user = interaction.guild.get_member(user_id)

        # Handle the selected option
        await interaction.response.send_message(f"You selected: {select_menu.values[0]}", ephemeral=True)

        # Provide instructions on how to create a ticket using Ticket Tool Bot
        await interaction.followup.send(f"To create a ticket related to {select_menu.values[0]} using Ticket Tool Bot, use the command: `$new {select_menu.values[0]}`")

        # Optionally, you can provide additional information or instructions

        # Create a new ticket with a unique ticket number (if necessary)
        # ticket_number = f"{select_menu.values[0]}-{len(bot.tickets) + 1}"
        # bot.tickets[ticket_number] = {
        #     "user_id": user.id,
        #     "selected_cryptocurrency": select_menu.values[0],
        #     "ticket_messages": [interaction.message.id],
        # }

        # Send a message indicating that the ticket was created (if necessary)
        # ticket_message = await interaction.channel.send(f"✔ Ticket Created ⁠{ticket_number}\nOnly you can see this • Dismiss message")

        # Add the ticket message to the list of ticket messages (if necessary)
        # bot.tickets[ticket_number]["ticket_messages"].append(ticket_message.id)

        # Additional steps for handling the ticket and redirecting users can be added here
        # For example, you can add reactions to the ticket_message for specific actions

# Initialize a dictionary to store ticket information
bot.tickets = {}

# Initialize a dictionary to store the message IDs associated with dropdowns
bot.dropdown_message_ids = {}






import discord
from discord.ext import commands
from common import bot

def setup_crypto_channel(bot):
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