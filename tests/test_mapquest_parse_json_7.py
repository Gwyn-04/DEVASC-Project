import pytest
from mapquest_parse_json_7 import output




def test_output():
    assert output("Washington, D.C", "Baltimore, M.D") == 0
