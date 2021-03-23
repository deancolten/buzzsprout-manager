import json
import requests
from datetime import datetime


class Manager():
    """Manages http requests and responses as well as authorization.

   Attributes:
        id(str): Podcast Id.
        token(str): API Token.
        name(str): Optional name.
    """

    def __init__(self, id, token):
        """
       Constructor

        Parameters:
            id(str): Podcast Id.
            token(str): API Token.
            name(str): Optional name.
        """
        self.id = id
        self.token = token

        self.base_url = f"https://www.buzzsprout.com/api/{id}"
        self.access_params = {'api_token': self.token}

        self.cache_headers = None

    def test_api(self):
        """Returns requests.response object for GET request to Buzzsprout API"""

        test_response = requests.get(
            f"{self.base_url}/episodes.json", self.access_params)
        return test_response

    def ok(self):
        """Checks for Response 200 and returns Bool"""

        test_response = requests.get(
            f"{self.base_url}/episodes.json", self.access_params)
        return test_response.ok

    def update(self):
        """Requests all episode objects from API and caches the response."""

        headers = self.cache_headers
        response = requests.get(
            url=f"{self.base_url}/episodes.json",
            headers=headers,
            params=self.access_params
        )
        if response.ok:
            if response.status_code == 200:
                e_list = []
                for i in response.json():
                    e_list.append(Episode(**i))
                self.cache_headers = {
                    'If-None-Match': response.headers['ETag'],
                    'If-Modified-Since': response.headers['Last-Modified']
                }
                self.cache_episodes = EpisodeGroup(*e_list)
        else:
            raise ConnectionError(f"Response {response.status_code}")

    def get_all_episodes(self):
        """Checks for update, and then returns all episodes in an Episode Group"""
        self.update()
        if self.cache_episodes:
            return self.cache_episodes
        else:
            # ****** Some type of exception here???********
            return None

    def get_episode_by_id(self, id):
        """Uses an episode id parameter to return a single Episode object"""

        response = requests.get(
            f"{self.base_url}/episodes/{id}.json", self.access_params)
        if response.ok:
            return Episode(**response.json())
        else:
            return False

    def get_episode_by_date(self, date):
        """Returns first episode that matches the given datetime object argument."""

        if type(date) != datetime:
            raise TypeError("get_episode_by_date requires a datetime object")
        e_group = self.get_all_episodes()
        if e_group:
            for e in e_group:
                if e.get_date() == date:
                    return e
            return False
        else:
            return False

    def update_episode(self, episode, **kwargs):
        """Update episode information with given key value pairs."""

        if type(episode) == Episode:
            f_id = episode.id
        elif id != None:
            f_id = id
        else:
            raise Exception("Must provide an episode object or id")

        headers = {"Content-Type": "application/json"}
        payload = json.dumps(kwargs)
        response = requests.put(
            url=f"https://www.buzzsprout.com/api/{self.id}/episodes/{f_id}.json",
            headers=headers,
            data=payload,
            params=self.access_params
        )
        self.update()
        return response.ok

    def update_episode_audio(self, episode, file_path=None, public=False):
        """
        Updates episode's previous audio file. By default, this sets the episode to private. 
        Set public to True to keep episode public after upload.
        """

        if type(episode) == Episode:
            f_id = episode.id
        elif id != None:
            f_id = id
        else:
            raise Exception("Must provide an episode object or id")
        payload = episode.get_existing_data()
        files = [('audio_file', open(file_path, 'rb'))]
        response = requests.put(
            url=f"{self.base_url}/episodes/{f_id}.json",
            data=payload,
            params=self.access_params,
            files=files
        )
        if public:
            self.set_episode_public(id=f_id)
        self.update()
        return response

    def update_episode_artwork(self, episode, file_path=None, public=False):
        """Updates episode's previous artwork file."""

        if type(episode) == Episode:
            f_id = episode.id
        elif id != None:
            f_id = id
        else:
            raise Exception("Must provide an episode object or id")
        payload = episode.get_existing_data()
        files = [('artwork_file', open(file_path, 'rb'))]
        response = requests.put(
            url=f"{self.base_url}/episodes/{f_id}.json",
            data=payload,
            params=self.access_params,
            files=files
        )
        if public:
            self.set_episode_public(id=f_id)
        self.update()
        return response

    def set_episode_private(self, episode=None, id=None):
        """Set episode private attribute to True. Takes either an Episode object or episode id as an argument"""

        if type(episode) == Episode:
            f_id = episode.id
        elif id != None:
            f_id = id
        else:
            raise Exception("Must provide an episode object or id")

        headers = {"Content-Type": "application/json"}
        payload = json.dumps({'private': "true"})
        response = requests.put(
            url=f"https://www.buzzsprout.com/api/{self.id}/episodes/{f_id}.json",
            headers=headers,
            data=payload,
            params=self.access_params
        )
        self.update()
        return response.ok

    def set_episode_public(self, episode=None, id=None):
        """Set episode private attribute to False. Takes either an Episode object or episode id as an argument"""

        if type(episode) == Episode:
            f_id = episode.id
        elif id != None:
            f_id = id
        else:
            raise Exception("Must provide an episode object or id")

        headers = {"Content-Type": "application/json"}
        payload = json.dumps({'private': "false"})
        response = requests.put(
            url=f"https://www.buzzsprout.com/api/{self.id}/episodes/{f_id}.json",
            headers=headers,
            data=payload,
            params=self.access_params
        )
        self.update()
        return response.ok

    # *****NOT WORKING******
        # def delete_episode(self, episode=None, id=None):
        #     """Delete Episode. Takes either an Episode object or episode id as an argument"""

        #     if type(episode) == Episode:
        #         f_id = episode.id
        #     elif id != None:
        #         f_id = id
        #     else:
        #         raise Exception("Must provide an episode object or id")

        #     headers = {"Content-Type": "application/json"}
        #     response = requests.get(
        #         url=f"https://www.buzzsprout.com/api/{self.id}/episodes/{f_id}.json",
        #         headers=headers,
        #         params=self.access_params
        #     )
        #     self.update()
        #     return response

    def post_episode(self, episode, audio_file_path=None, artwork_file_path=None):
        """Posts episode to Buzzsprout. If file_path is included, the file will be uploaded."""
        files = []
        if audio_file_path:
            files.append(('audio_file', open(audio_file_path, 'rb')))
        if artwork_file_path:
            files.append(('artwork_file', open(artwork_file_path, 'rb')))
        payload = episode.get_existing_data()
        if files:
            response = requests.post(
                url=f"{self.base_url}/episodes.json",
                data=payload,
                params=self.access_params,
                files=files
            )
        else:
            response = requests.post(
                url=f"{self.base_url}/episodes.json",
                data=payload,
                params=self.access_params
            )
        self.update()
        self.set_episode_public(episode=episode)
        return response


class EpisodeGroup():
    """Class for managing groups of Episode objects."""

    def __init__(self, *args):
        for i in args:
            if type(i) != Episode:
                raise TypeError(
                    "EpisodeGroup can only take episode objects as arguments")
        self.content = [*args]

    def __iter__(self):
        for elem in self.content:
            yield elem

    # def __repr__(self):
    #     return str(self.content)

    def __getitem__(self, episode):
        return self.content[episode]

    def add(self, *args):
        for i in args:
            if type(i) != Episode:
                raise TypeError(
                    "EpisodeGroup can only take episode objects as arguments")
        self.content.append(*args)

    def remove(self, index):
        self.content.pop(index)

    def pop(self, index=None):
        self.content.pop(index=index)

    def num_episodes(self):
        t = 0
        for _ in self.content:
            t += 1
        return t

    def newest(self):
        n_ep = None
        n_date = datetime(1800, 1, 1)
        for i in self.content:
            if i.get_date() > n_date:
                n_ep = i
                n_date = i.get_date()
        return n_ep

    def oldest(self):
        o_ep = None
        o_date = datetime(4000, 1, 1)
        for i in self.content:
            if i.get_date() < o_date:
                o_ep = i
                o_date = i.get_date()
        return o_ep


class Episode():
    """Class for Buzzsprout episode meta-data"""

    ATTR_STRINGS = [
        'id',
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
        'total_plays'
    ]

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.audio_url = kwargs.get('audio_url')
        self.description = kwargs.get('description')
        self.summary = kwargs.get('summary')
        self.artist = kwargs.get('artist')
        self.tags = kwargs.get('tags')
        self.published_at = kwargs.get('published_at')
        self.duration = kwargs.get('duration')
        self.hq = kwargs.get('hq')
        self.magic_mastering = kwargs.get('magic_mastering')
        self.guid = kwargs.get('guid')
        self.inactive_at = kwargs.get('inactive_at')
        self.episode_number = kwargs.get('episode_number')
        self.season_number = kwargs.get('season_number')
        self.explicit = kwargs.get('explicit')
        self.private = kwargs.get('private')
        self.total_plays = kwargs.get('total_plays')

    def __repr__(self):
        return(f"Episode Object - ID:{self.id} - Title: {self.title}")

    def get_date(self):
        """Returns datetime object for episode's 'published_at' date"""

        try:
            dt_string = self.published_at.split('T')[0]
            dt_object = datetime.strptime(dt_string, '%Y-%m-%d')
            return(dt_object)
        except:
            raise AttributeError("Episode has no published_at attribute")

    def get_existing_data(self):
        """Returns dict of episode attributes that != None"""

        existing_data = {}
        for i in self.ATTR_STRINGS:
            x = getattr(self, i)
            if x is not None:
                existing_data[i] = x
        return existing_data

    def get_all_data(self):
        """Returns dictionary of all episode attributes, including None values"""

        all_data = {}
        for i in self.ATTR_STRINGS:
            x = getattr(self, i)
            all_data[i] = x

        return all_data


if __name__ == "__main__":
    pass
