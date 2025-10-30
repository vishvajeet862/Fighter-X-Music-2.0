import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQGnZGQAgadEUh1aW8YdSiQwc1Y3rHqgMd8YDylWbgjNl-lCDzBX4tOCLhHWLZBWwM3pPF8Ya5AfOnRYkLEQL7pvwyHWE-9t-aXx6wNm3cz5d79pC_Z9JjKbkHz-HxOGsu2OAvh42iORElaT5andUAqLXfnBkQmcPYrRgAsWA1eaDnWADaU9HJqR4MlX5jPh-rTRA6hLvqPMM81nQbGRdq3SfmD9IDEXnt4f0d_GTrfqe20Djv5keMrA5ep0L0nIkX-qAerFsKpwkcu02TG75hwDVsqrQrV0ytTqvELAs9Sa5idHDGJyALRmoCwZz9J5zpmLRCA0X-VXY6Om4Uxv6nvARSbXNAAAAAG6EnFwAA")
BOT_TOKEN = getenv("8376904204:AAFNW9X3mvw_FwTUkc8PsFwhjBRC37QkEsY")
BOT_NAME = getenv("𝐅𝗂𝗀ɦ𝗍𝖾𝗋 𝐗 𝐌υ𝗌𝗂𝖼")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GARUD_NETWORK")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("27747428"))
API_HASH = getenv("b56b68347922ff0d053e4d77db849d63")
BOT_USERNAME = getenv("@Fighters_Legend_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "FIGHTER MUSIC")
OWNER_NAME = getenv("OWNER_NAME", "Silentkiller905")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GARUD_SUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8328453402").split()))
