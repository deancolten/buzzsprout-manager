from bsm import bsm
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
TOKEN = os.environ.get("TTOKEN")
ID = os.environ.get("TID")

manager = bsm.Manager(ID, TOKEN)

<<<<<<< HEAD
eps = manager.get_all_episodes()

print(eps[0])
=======
episodes = manager.get_all_episodes()
for i in episodes:
    print(i.title)
    print(i.duration)
>>>>>>> b85384a64f52c2253d7e39419af23474f0f8f69c
