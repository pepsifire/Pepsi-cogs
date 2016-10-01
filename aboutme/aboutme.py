from discord.ext import commands


class AboutMe:
    """Tells stuff about you"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def aboutme(self, ctx):
        """Tells stuff about you"""
        name = ctx.message.author.name
        userid = ctx.message.author.id
        bot = str(ctx.message.author.bot)
        join_date = ctx.message.author.created_at
        top_role = ctx.message.author.top_role
        await self.bot.say("```" + "\nInfo about: " + name + "\n"
                           + "ID: " + userid + "\n" +
                           "Are you a bot?: " + bot + "\n"
                           + "You joined at: " + str(join_date) + "\n"
                           + "Your highest role is: " + str(top_role)
                           + "\n```")


def setup(bot):
    bot.add_cog(AboutMe(bot))
