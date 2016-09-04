import discord


class chat_responder:
    """Cures eye cancer and does other things"""

    def __init__(self, bot):
        self.bot = bot

    async def not_static(self, message):
        """Cures eye cancer"""
        if message.content == "PassTheBleach":
            image = "https://i.imgur.com/b64G8Fx.png"
        if message.content == "werks tm":
            image = "https://i.imgur.com/Ddp7QIz.png"
        if message.content == "such sekret doge":
            image = "https://i.imgur.com/tJEEI53.jpg"

        await self.bot.send_message(message.channel, image)


def setup(bot):
    n = chat_responder(bot)
    bot.add_listener(n.not_static, "on_message")
    bot.add_cog(n)
