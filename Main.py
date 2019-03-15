#Paul Woody - 2019
#www.github.com/pawoody
#www.linkedin.com/paul-woody

import requests
import discord
client = discord.Client()
from bs4 import BeautifulSoup4
from discord.ext import commands

class BarlesCharkley:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def rude(self, ctx):
        await self.bot.delete_message(ctx.message)
        response = requests.get(
            "http://www.robietherobot.com/insult-generator.htm").text
        site = BeautifulSoup4(response, "lxml")
        await self.bot.send_message(
            ctx.message.channel, "{}!".format(
                site.select("div.rude")[0].text))


def setup(bot):
    bot.add_cog(BarlesCharkley(bot))

token = os.environ.get("DISCORD_BOT_SECRET")
client.run()    