from bsm import bsm
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get("TTOKEN")
ID = os.environ.get("TID")

manager = bsm.Manager(ID, TOKEN)

print(manager.test_api())
