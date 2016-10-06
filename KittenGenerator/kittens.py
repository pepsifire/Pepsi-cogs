from discord.ext import commands
from bs4 import BeautifulSoup
import aiohttp


class KittenGenerator:
    """Get all the kittens in the world!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kitten(self):
        """Kittens."""
        url = "http://thecatapi.com/api/images/get?format=html&type=jpg"
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            image = soupObject.find('img', src=True)
            kittens = image['src']
            await self.bot.say(kittens)
        except:
            await self.bot.say("Error, no kittens found.")


def setup(bot):
    bot.add_cog(KittenGenerator(bot))
