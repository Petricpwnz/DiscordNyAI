import pyotp
import os

from dotenv import load_dotenv

load_dotenv()
twitch_2fa_key = os.environ['twitch_2fa_key']
totp = pyotp.TOTP(twitch_2fa_key)


def get_token():
    # generates a 2FA sign-in token from the secret key provided
    return totp.now()
