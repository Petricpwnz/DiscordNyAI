import sys
import shared

from discord.ext import commands

from modules.utils import create_logger

GClogger = create_logger('generic_commands', 'info', 'data/logs/')


class GenericCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check_any(commands.has_role(int(shared.get_config()['bot']['FAFLiveTokenRole'])), commands.has_permissions(administrator=True))
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send('Still here')

    @commands.command(name='shutdown')
    @commands.has_permissions(administrator=True)
    async def shutDown(self, ctx):
        text = 'Shutting the bot down'
        try:
            GClogger.info(text)
            await ctx.send(text)
            sys.exit()
        except Exception:
            GClogger.info(text)
            await ctx.send(text)
            sys.exit()


def setup(bot):
    bot.add_cog(GenericCommands(bot))
