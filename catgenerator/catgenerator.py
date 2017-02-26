import discord
from discord.ext import commands
from urllib.request import urlopen


class KittenGenerator:
    """Get all the kittens (and cats) in the world!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kitten(self):
        """Kittens. (and cats)"""
        url = "http://thecatapi.com/api/images/get?format=src&type=jpg"
        try:
            req = urlopen(url)
            embed = discord.Embed(description="")
            embed.set_image(url=req.geturl())
            await self.bot.say(embed=embed)
        except:
            await self.bot.say("Error, no kittens found.")


def setup(bot):
    bot.add_cog(KittenGenerator(bot))
