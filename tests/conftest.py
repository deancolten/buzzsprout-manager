import pytest
from dotenv import load_dotenv
from bsm import Manager, Episode, EpisodeGroup
import os

load_dotenv()
TEST_ID = os.environ.get('TEST_ID')
TEST_ID_2 = os.environ.get('TEST_ID_2')
FAIL_ID = os.environ.get('FAIL_ID')
TEST_TOKEN = os.environ.get('TEST_TOKEN')
FAIL_TOKEN = os.environ.get('FAIL_TOKEN')


@pytest.fixture
def creds():
    return (TEST_ID, TEST_TOKEN)


@pytest.fixture
def second_creds():
    return (TEST_ID_2, TEST_TOKEN)


@pytest.fixture
def bad_ID_creds():
    return (FAIL_ID, TEST_TOKEN)


@pytest.fixture
def bad_TOKEN_creds():
    return (TEST_ID, FAIL_TOKEN)


@pytest.fixture
def manager():
    return Manager(TEST_ID, TEST_TOKEN)


@pytest.fixture
def manager2():
    return Manager(TEST_ID_2, TEST_TOKEN)


@pytest.fixture
def episode():
    return Episode(**{
        'title': "Test Episode",
        'description': "Test Description"
    })
