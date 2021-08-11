import configobj

from discord.ext import commands

from modules.twoFA import get_token
from modules.utils import create_logger
from modules.decorators import *

config = configobj.ConfigObj(r'../config.ini')
TSlogger = create_logger('token_stuff', 'info', 'data/logs/')


class TokenStuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    FAFLive_token_role = int(config['bot']['FAFLiveTokenRole'])
    FAFLive_token_channel = int(config['bot']['FAFLiveTokenChannel'])

    @commands.command(name='token')
    @commands.has_role(FAFLive_token_role)
    @commands.guild_only()
    @commands.check(FAFLive_2fa_channel)
    async def getToken(self, ctx):
        TSlogger.info(f'Sent a token by request of {ctx.author.name}, id {ctx.author.id}')
        await ctx.send(get_token())

    @commands.command(name='registertokenchannel')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def registerTokenChannel(self, ctx, id=None):
        try:
            channel_id = int(id) or ctx.channel.id
        except Exception:
            channel_id = ctx.channel.id

        try:
            FAFLive_token_channel = channel_id
            config['bot']['FAFLiveTokenChannel'] = FAFLive_token_channel
            config.write()
            await ctx.send(f'Set {self.bot.get_channel(FAFLive_token_channel).name} as the FAFLive token channel.')
        except Exception as e:
            TSlogger.warning(f'Failed setting up a token channel. {str(e)}')
            await ctx.send('Failed setting up a token channel.')

    @commands.command(name='registertokenrole')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def registerTokenRole(self, ctx, id=None):
        try:
            FAFLive_token_role = int(id)
            config['bot']['FAFLiveTokenRole'] = FAFLive_token_role
            config.write()
            await ctx.send(f'Set role with the ID of {FAFLive_token_role} as the FAFLive token role.')
        except Exception as e:
            TSlogger.warning(f'Failed setting up a token role. {str(e)}')
            await ctx.send('Failed setting up a token role. Have you provided the role ID?')


def setup(bot):
    bot.add_cog(TokenStuff(bot))
