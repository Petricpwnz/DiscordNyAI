import configobj


def FAFLive_2fa_channel(ctx):
    # TODO expand into a generic decorator for any channel check and proper import
    _config = configobj.ConfigObj(r'../config.ini')
    _FAFLIVE_TOKEN_CHANNEL = int(_config['bot']['FAFLiveTokenChannel'])
    return ctx.channel.id == _FAFLIVE_TOKEN_CHANNEL
