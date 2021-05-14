from bsm import Manager, Episode, EpisodeGroup
from dotenv import load_dotenv
import os

load_dotenv()
ID = os.environ.get("ID")
TOKEN = os.environ.get("TOKEN")

manager = Manager(ID, TOKEN)

print(manager.test_api())

ep = Episode(**{'title': "test upload"})

res = manager.post_episode(ep, 'testfile.mp3', None)
print(res)
