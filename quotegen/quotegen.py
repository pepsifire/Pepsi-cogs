import random
from discord.ext import commands
from redbot.core import Config
from redbot.core import checks
from tabulate import tabulate


class Setup:
    try:
        from tabulate import tabulate

        tabulateAvailable = True
    except ModuleNotFoundError:
        tabulateAvailable = False


class QuoteGenerator:
    """Quote generator."""

    def __init__(self, bot):
        self.bot = bot
        self.settings = Config.get_conf(self, identifier=0xDEADBEEF, force_registration=True)
        self.settings.register_global(
            quotes=["THIS IS SPARTA!", "The cake is a lie"]
        )
        self.quotes = self.settings

    @commands.command()
    async def quote(self, ctx):
        """Spits out quotes"""
        quote = await self.settings.quotes()
        await ctx.send(random.choice(quote))

    @commands.group(name="setquote", pass_context=True)
    async def _setquote(self, ctx):
        """Quote list management"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help()

    @_setquote.command(no_pm=True)
    @checks.is_owner()
    async def add(self, ctx, quote: str):
        """Add quotes"""
        async with self.settings.quotes() as quotes:
            quotes.append(quote)

        await ctx.send("Added \"" + quote + "\" to quotes.")

    @_setquote.command(no_pm=True)
    @checks.is_owner()
    async def delete(self, ctx, quote: str):
        """Delete quotes. Get the quote name with "[p]quotelist" """
        try:  # If it's empty python raises KeyError.
            async with self.settings.quotes() as quotes:
                quotes.remove(quote)
            await ctx.send("Quote \"" + quote + "\" deleted.")
        except KeyError:
            await ctx.send("Delete quotes. Get the quote name with \"[p]quotelist\"")

    @commands.command()
    async def quotelist(self, ctx):
        """List quotes"""
        quote = await self.settings.quotes()
        tabulated_list = tabulate({"Quotes": quote}, headers='keys',
                                  tablefmt='simple')
        await ctx.send("```\n" + tabulated_list + "```\n")
