import discord
from discord.ext import commands


class AboutMe:
    """Tells stuff about people"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def aboutme(self, ctx, user: discord.Member=None):
        """Tells stuff about people"""
        author = ctx.message.author
        if not user:
            user = author

        name = user.name
        userid = user.id
        if user.bot is False:
            bot = "Nope"
        else:
            bot = "Beep Boop"
        join_date = user.created_at.strftime("%d %b %Y")
        top_role = user.top_role
        data = discord.Embed(title="")
        data.set_author(name="{}".format(user), icon_url=user.avatar_url)
        data.add_field(name="Name", value=name)
        data.add_field(name="User ID", value=userid)
        data.add_field(name="Am i a bot?", value=bot)
        data.add_field(name="Discord Join Date", value=join_date)
        data.add_field(name="Top Role", value=top_role)
        data.set_thumbnail(url=user.avatar_url)
        await self.bot.say(embed=data)


def setup(bot):
    bot.add_cog(AboutMe(bot))
