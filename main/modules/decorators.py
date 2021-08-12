import shared

from modules.utils import create_logger

dec_logger = create_logger('generic_commands', 'info', 'data/logs/')


def FAFLive_2fa_channel(ctx):
    # TODO expand into a generic decorator for any channel check
    return ctx.channel.id == int(shared.get_config()['bot']['FAFLiveTokenChannel'])


def custom_has_roles(roles={}):
    # put as the last decorator to make sure all non-custom checks go through
    def custom_has_roles_wrapper(func):
        async def custom_has_roles_inner(*args, **kwargs):
            _roles = roles
            if 'faflive' in roles:
                _roles = shared.get_config()['bot']['FAFLiveTokenRole']

            ctx = [*args][1]
            for role in ctx.message.author.roles:
                if str(role.id) in _roles:
                    await func(*args, **kwargs)
            dec_logger.info(f'{ctx.message.author.name} has no roles with IDs {roles}')
            return
        return custom_has_roles_inner
    return custom_has_roles_wrapper
