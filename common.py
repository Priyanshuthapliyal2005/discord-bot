# common.py
import discord
from discord.ext import commands

class MiddlemanBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize a dictionary to store ticket information
        self.tickets = {}

        # Initialize a dictionary to store the message IDs associated with dropdowns
        self.dropdown_message_ids = {}
