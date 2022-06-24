import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, humanize_list
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu
import aiohttp

BaseCog = getattr(commands, "Cog", object)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class Catgirl(BaseCog):

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.catgirlapi = "https://nekos.best/api/v2/neko"
        self.nsfwcatgirlapi = "http://api.nekos.fun:8080/api/lewd" #tnx rosie
        self.error_message = "Error."

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def catgirl(self, ctx):
        try:
            async with self.session.get(self.catgirlapi) as r:
                result = await r.json()
            await ctx.send(result['url'])
        except:
            await ctx.send(result)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def nsfwcatgirl(self, ctx):
        try:
            async with self.session.get(self.nsfwcatgirlapi) as r:
                result = await r.json()
            await ctx.send(result['image'])
        except:
            await ctx.send(result)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
