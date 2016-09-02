import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO, fileIO
from cogs.utils import checks
import os
import random
try:
    from tabulate import tabulate
    tabulateAvailable = True
except:
    tabulateAvailable = False

default_quotes = {'sparta': "THIS IS SPARTA!", 'cake': "The cake is a lie."}


class QuoteGenerator:
    """Quote generator."""

    def __init__(self, bot):
        self.bot = bot
        self.quotes = dataIO.load_json("data/quote_generator/quotes.json")

    @commands.command()
    async def quote(self):
        """Spits out quotes"""
        await self.bot.say(random.choice(list(self.quotes.values())))

    @commands.command()
    @checks.is_owner()
    async def addquote(self, name: str, quote: str):
        """Add quotes"""
        self.quotes[name] = quote
        await self.bot.say("Added \"" + quote + "\" to quotes.")
        dataIO.save_json("data/quote_generator/quotes.json", self.quotes)

    @commands.command()
    @checks.is_owner()
    async def delquote(self, name: str):
        """Delete quotes"""
        del self.quotes[name]
        dataIO.save_json("data/quote_generator/quotes.json", self.quotes)
        await self.bot.say("Quote \"" + name + "\" deleted.")

    @commands.command()
    async def listquote(self):
        """List quotes"""
        tabulated_list = tabulate({"Name": self.quotes.keys(), "Quotes": self.quotes.values()}, headers='keys', tablefmt='simple')
        await self.bot.say("```\n" + tabulated_list + "```\n")  # Todo make this nicer


def check_folders():
    if not os.path.exists("data/quote_generator/"):
        print("Creating data/quote_generator folder")
        os.makedirs("data/quote_generator")


def check_files():
    f = "data/quote_generator/quotes.json"
    if not fileIO(f, "check"):
        print("Creating quote.json")
        fileIO(f, "save", default_quotes)


def setup(bot):
        if tabulateAvailable:
            check_folders()
            check_files()
            bot.add_cog(QuoteGenerator(bot))
        else:
            raise RuntimeError("You need to run `pip3 install tabulate`")