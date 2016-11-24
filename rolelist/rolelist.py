from discord.ext import commands


class Rolelist:
    """List server roles"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rolelist(self, ctx):
        """List server roles"""
        try:
            data = "```"
            for r in ctx.message.author.server.roles:
                data += r.name
                data += "\n"
            data += "```"
            await self.bot.say(data)
        except:
            await self.bot.say("Insufficient permissions.")


def setup(bot):
    bot.add_cog(Rolelist(bot))
