from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "7438136782:AAEbPfdeXOVIeAqPXQJNEtuYWxM0x7D0fIE")
SESSION_NAME = getenv("SESSION_NAME", "1AZWarzMBu7lTg8uHrBDt_9r6CHnrJHtkZGyjaXYE4X_B3LNP7MaTRR_DalqX7S4Qp_ox0TOxdkzolPh85ef_iWbSzNrY78c7KmsKHqUEdPfK_7KbMkhNUItbRnxejyUTfr7xr19kjBEp1Tj3ImNAWs3V7IckhbMay6RwFGF17kREQH_fhsIgRheDHjBy7NrzyGQm-HuCgxvc6ZuPG3Veoq6BITccVq3q28QzE4aRWPM6t1lzGS1xpocWzmyHKU-UzuTSblDvJwMwEW5Xp0QPM84XWPNdH3NeG2Hty5Cu-UYrD3_zwr3mAjd_8eT78e-06JVU1Cv3cbMPXbnSwLVp5k1yjuHVgn8=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Mmh_md0")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Djejejejwjbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6241442696").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
