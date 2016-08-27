import discord
from discord.ext import commands

class Invite_bot:
    """Does stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Invite(self):
        """Get oauth url"""
        perms = discord.Permissions().all()
        data = await self.bot.application_info()
        name = data.name
        desc = data.description
        owner = data.owner.name
        bot_url = discord.utils.oauth_url(data.id, permissions=perms, server=None, redirect_uri=None)
        msg = "Hello! My name is " + name + "!\n"
        msg += "Note:" + desc + "\n"
        msg += "If you would like to invite me to your server, click here: \n"
        msg += bot_url + "\n"
        msg += "Please allow all permissions for full usage of the bot"
        await self.bot.say(msg)


def setup(bot):
    bot.add_cog(Invite_bot(bot))
