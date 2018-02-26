import discord
from discord.ext import commands
from urllib.request import urlopen


class CatGenerator:
    """Get all the kittens (and cats) in the world!"""

    def __init__(self):
        self.url = "http://thecatapi.com/api/images/get?format=src&type=jpg"

    @commands.command()
    async def cat(self, ctx):
        """Pictures of cats!"""

        try:
            req = urlopen(self.url)
            embed = discord.Embed(description="Cats!")
            embed.set_image(url=req.geturl())
            await ctx.send(embed=embed)
        except:
            await ctx.send("Error, no kittens found.")


