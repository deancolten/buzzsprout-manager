from bsm import Manager, EpisodeGroup


def test_update(creds):

    m = Manager(creds[0], creds[1])
    # cache empty
    assert m.cache_episodes == None
    assert m.cache_headers == None

    assert m._update() == 200
    # header cached properly, response 304
    assert m._update() == 304

    # check cache
    assert isinstance(m.cache_episodes, EpisodeGroup)
    assert isinstance(m.cache_headers, dict)

    m2 = Manager(creds[0], creds[1])

    # Give m2 a full cache and test for proper response
    m2.cache_episodes, m2.cache_headers = m.cache_episodes, m.cache_headers
    assert m2._update() == 304

    m3 = Manager(creds[0], creds[1])

    # Give m3 only headers cache, and make sure response is 200 not 304
    m3.cache_headers = m.cache_headers
    assert m3._update() == 200
