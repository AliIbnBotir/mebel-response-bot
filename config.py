import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.environ["BOT_TOKEN"]

ADMIN_IDS: set[int] = {
    int(uid.strip())
    for uid in os.environ["ADMIN_IDS"].split(",")
    if uid.strip()
}

GROUP_ID: int = int(os.environ["GROUP_ID"])
