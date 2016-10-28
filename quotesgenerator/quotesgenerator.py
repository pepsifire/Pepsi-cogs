import os
import random

from __main__ import send_cmd_help
from cogs.utils import checks
from cogs.utils.dataIO import dataIO, fileIO
from discord.ext import commands

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

    @commands.group(name="setquote", pass_context=True)
    async def _setquote(self, ctx):
        """Quote list management"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_setquote.command(pass_context=True, no_pm=True)
    @checks.is_owner()
    async def add(self, ctx, name: str, quote: str):
        """Add quotes"""
        self.quotes[name] = quote
        await self.bot.say("Added \"" + quote + "\" to quotes.")
        dataIO.save_json("data/quote_generator/quotes.json", self.quotes)

    @_setquote.command(pass_context=True, no_pm=True)
    @checks.is_owner()
    async def delete(self, ctx, name: str):
        """Delete quotes. Get the quote name with "[p]listquotes" """
        try:  # If it's empty python raises KeyError.
            del self.quotes[name]
            dataIO.save_json("data/quote_generator/quotes.json", self.quotes)
            await self.bot.say("Quote \"" + name + "\" deleted.")
        except KeyError:
            await self.bot.say("```Delete quotes. Get the quote name with \"[p]listquotes\" ```")

    @commands.command()
    async def quotelist(self):
        """List quotes"""
        tabulated_list = tabulate({"Name": self.quotes.keys(), "Quote": self.quotes.values()}, headers='keys',
                                  tablefmt='simple')
        await self.bot.say("```\n" + tabulated_list + "```\n")


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
