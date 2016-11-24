import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import aiohttp


class KittenGenerator:
    """Get all the kittens (and cats) in the world!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kitten(self):
        """Kittens. (and cats)"""
        url = "http://thecatapi.com/api/images/get?format=html&type=jpg"
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            image = soupObject.find('img', src=True)
            kittens = image['src']
            embed = discord.Embed(description="")
            embed.set_image(url=kittens)
            await self.bot.say(embed=embed)
        except:
            await self.bot.say("Error, no kittens found.")


def setup(bot):
    bot.add_cog(KittenGenerator(bot))
