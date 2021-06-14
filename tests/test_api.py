from bsm import Manager


def test_api_good(manager):
    assert manager.ok()


def test_api_badID(bad_ID_creds):
    assert not Manager(bad_ID_creds[0], bad_ID_creds[1]).ok()


def test_api_badTOKEN(bad_TOKEN_creds):
    assert not Manager(bad_TOKEN_creds[0], bad_TOKEN_creds[1]).ok()
