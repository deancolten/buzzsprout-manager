# Buzzsprout-Manager

## Summary

Buzzsprout Manager is a (somewhat) complete python wrapper for the Buzzsprout Podcast Hosting API. It currently supports most of the functionality of buzzsprout's web UI, including uploading/creating new episodes, retrieving information from existing episodes, as well as updating information or changing an episode's private status. 

## Getting Started

#### Installation

`pip install buzzsprout-manager`

#### Basic Usage
```python
from bsm import bsm

ID = 'My Podcast ID'
TOKEN = 'My API Token'
 
manager = bsm.Manager(ID, TOKEN) # Init

episodes = manager.get_all_episodes() # Get all episodes as EpisodeGroup object

newest_episode = episodes[0] # Get Episode object

print(newest_episode.title) # "My Podcast Title"

manager.update_episode(     # Update given episode with kwarg attributes
    newest_episode,
     **{'title': "Updated Title", 'description': "*descriptive text*"}
     ) 
manager.get_all_episodes()[0].title # "Updated Title"
```

## bsm.Episode
The following members can be retrieved and/ or modified:
```python
['id',
'title',
'audio_url',
'description',
'summary',
'artist',
'tags',
'published_at',
'duration',
'hq',
'magic_mastering',
'guid',
'inactive_at',
'episode_number',
'season_number',
'explicit',
'private',
'total_plays']

``` 