import discord
from discord.ext import commands
from discord.ui import Select

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
        dropdown = Select(
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
        await ctx.send(embed=embed, view=discord.ui.View().add_item(dropdown))

    @bot.event
    async def on_select_option(interaction: discord.Interaction, select_menu: discord.Select):
        # Handle the selected option
        await interaction.response.send_message(f"You selected: {select_menu.values[0]}", ephemeral=True)
