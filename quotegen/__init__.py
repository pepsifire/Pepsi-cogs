from .quotegen import QuoteGenerator
from .quotegen import Setup


def setup(bot):
    if Setup.tabulateAvailable:
        bot.add_cog(QuoteGenerator(bot))
    else:
        raise RuntimeError("You need to run `pip3 install tabulate`")
