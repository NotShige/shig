from .bedrockstatus import BedrockStatus


def setup(bot):
    bot.add_cog(BedrockStatus(bot))
