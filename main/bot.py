import os
import configobj

from dotenv import load_dotenv
from discord.ext import commands
from modules.utils import create_logger

# TODO cant pass config as argument to cogs so import there again, figure out how to use the package=None arg for setup function to maybe fix this
try:
    config = configobj.ConfigObj(r'../config.ini')
    BOT_NAME = config['bot']['Username']
except Exception as e:
    print(f'Failed parsing config.ini {str(e)}')
    BOT_NAME = 'Somebotname'

logger = create_logger(BOT_NAME, 'info', 'data/logs/')

load_dotenv()
TOKEN = os.environ.get('discord_bot_token')

COGS = ['cogs.GenericCommands', 'cogs.TokenStuff']
bot = commands.Bot(command_prefix='!')


# EVENTS
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    logger.info(f'Logged in as {bot.user}!')


@bot.event
async def on_command_error(ctx, error):
    logger.error(f'Error occured:\n{error}')


# COMMANDS
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, cog=None):
    if cog:
        try:
            bot.load_extension(cog)
            text = f'Loaded the {cog} cog.'
            logger.info(text)
            await ctx.send(text)
        except Exception as e:
            logger.warning(f'Failed to load the {cog} cog. {str(e)}')
            await ctx.send(f'Failed to load the {cog} cog.')


@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, cog=None):
    if cog:
        try:
            bot.unload_extension(cog)
            text = f'Unloaded the {cog} cog.'
            logger.info(text)
            await ctx.send(text)
        except Exception as e:
            logger.warning(f'Failed to unload the {cog} cog. {str(e)}')
            await ctx.send(f'Failed to unload the {cog} cog.')


@bot.command(name='reloadall')
@commands.has_permissions(administrator=True)
async def reloadAll(ctx, cog=None):
    for cog in COGS:
        try:
            bot.reload_extension(cog)
            text = f'Reloaded the {cog} cog.'
            logger.info(text)
            await ctx.send(text)
        except Exception as e:
            logger.warning(f'Failed to reload the {cog} cog. {str(e)}')
            await ctx.send(f'Failed to reload the {cog} cog.')


# OTHER
def load_necessary_cogs(_bot):
    # Loads them as extentions
    for cog in COGS:
        try:
            _bot.load_extension(cog)
            logger.info(f'Loaded the {cog} cog.')
        except Exception as e:
            logger.warning(f'Failed to load the {cog} cog. {str(e)}')


def run(_bot):
    load_necessary_cogs(_bot)
    _bot.run(TOKEN)


if __name__ == '__main__':
    run(bot)
