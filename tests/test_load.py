from dundie.core import load
from tests.constants import PEOPLE_FILE
def test_load():
    assert len(load(PEOPLE_FILE)) == 2