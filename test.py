from bsm import bsm
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
ID = os.environ.get("TID")
TOKEN = os.environ.get("TTOKEN")

manager = bsm.Manager(ID, TOKEN)

episodes = manager.get_all_episodes()
