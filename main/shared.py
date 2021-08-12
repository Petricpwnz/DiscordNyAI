import configobj


def get_config():
    # We get a new configobj every time because it's used across the bot and its cogs
    # and you cant pass args (the config obj) to cogs so the alternative would be reimporting and reassigning it everywhere
    # and we dynamically update the values with commands so we need to make sure we get the freshest version
    try:
        return configobj.ConfigObj(r'../config.ini')
    except Exception as e:
        print(f'Failed parsing config.ini {str(e)}')
        return None
