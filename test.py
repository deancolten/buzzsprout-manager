from bsm import Manager, Episode, EpisodeGroup
from dotenv import load_dotenv
import os

load_dotenv()
ID = os.environ.get("TID")
TOKEN = os.environ.get("TTOKEN")

manager = Manager(ID, TOKEN)

print(manager.test_api())

ep = Episode(**{'title': "test upload"})

new_ep = manager.get_episode_by_id('8561451')

res = manager.update_episode_audio(new_ep, 'testfile.mp3')

print(res.response.request.headers['content-type'])
