import random

from discord.ext import commands


class Highroller:
    """Double or nothing"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hiroll(self, ctx, agree: str):
        """Double your credits or lose them all. Type hiroll "i have a dream" to play."""
        bank = self.bot.get_cog('Economy').bank
        user = ctx.message.author
        result = random.randint(0, 1)

        if not agree.lower() == "i have a dream":
            await self.bot.say("Dream bigger! \nType \"i have a dream\" in with the quotes.")
            return
        else:
            pass
        if result == 0:
            await self.bot.say(user.mention + " lost all their credits!")
            bank.set_credits(user, 0)
        else:
            double = bank.get_balance(user) * 2
            await self.bot.say(user.mention + " won! Doubling their credits...")
            bank.set_credits(user, double)
            await self.bot.say("You have " + str(bank.get_balance(user)) + " credits now!")


def setup(bot):
    bot.add_cog(Highroller(bot))
