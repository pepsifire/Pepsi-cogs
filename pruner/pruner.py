from discord.ext import commands
from __main__ import send_cmd_help
from cogs.utils import checks


class Pruner:
    """Prune inactive members"""

    def __init__(self, bot):
        self.bot = bot

    @checks.admin_or_permissions(manage_server=True)
    @commands.group(name="pruner", pass_context=True)
    async def _pruner(self, ctx):
        """Prune members"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_pruner.command(pass_context=True)
    async def check(self, ctx, days_amount: int):
        """Check members to prune based on days"""
        this_server = ctx.message.author.server
        prune_amount = await self.bot.estimate_pruned_members(server=this_server, days=days_amount)
        await self.bot.say("Amount of members that would be pruned: " + str(prune_amount))

    @_pruner.command(pass_context=True)
    async def prune(self, ctx, days_amount: int):
        """Prune members"""
        this_server = ctx.message.author.server
        prune_amount = await self.bot.estimate_pruned_members(server=this_server, days=days_amount)  # I'm lazy
        await self.bot.prune_members(server=this_server, days=days_amount)
        await self.bot.say(str(prune_amount) + " inactive members pruned.")


def setup(bot):
    bot.add_cog(Pruner(bot))
