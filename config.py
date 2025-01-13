import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "29171167"))
API_HASH = os.environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7251898668"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "akmovieshubbackup")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002390475605"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://akre:akre@cluster0.gtpo3kw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/vT2.jpg")
