from bsm import Manager, Episode, EpisodeGroup
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
ID = os.environ.get("ID")
TOKEN = os.environ.get("TOKEN")

manager = Manager(ID, TOKEN)

print(manager.test_api())
