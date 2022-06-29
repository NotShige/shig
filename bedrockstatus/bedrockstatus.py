import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, humanize_list
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu
from mcstatus import BedrockServer

BaseCog = getattr(commands, "Cog", object)
serverip = "sg2.tortoises.studio:4004"
bdstatus = BedrockServer.lookup(serverip)

class BedrockStatus(BaseCog):

    def __init__(self, bot):
        self.bot = bot
        self.error_message = "Error."

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def bedrockstatus(self, ctx):
        try:
            async with bdstatus() as r:
                result = await r.json()
            await ctx.send(result)
        except:
            await ctx.send(self.error_message)


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
