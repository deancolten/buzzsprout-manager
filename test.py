from bsm import bsm
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
TOKEN = os.environ.get("TTOKEN")
ID = os.environ.get("TID")

manager = bsm.Manager(ID, TOKEN)

episodes = manager.get_all_episodes()
