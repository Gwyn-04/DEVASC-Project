import pytest
from mapquest_parse_json_7 import outprint




def test_outprint():
    assert outprint("Washington, D.C", "Baltimore, M.D") == 0
