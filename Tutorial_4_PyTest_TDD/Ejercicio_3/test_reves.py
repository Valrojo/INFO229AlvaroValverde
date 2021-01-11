import pytest

def reves(string):
    return string[::-1]

@pytest.mark.parametrize("qwe, ewq", [("alvaro", "oravla"),("ana", "ana"),("toyota", "atoyot")])
def test_reves(qwe,ewq):
    assert reves(qwe) == ewq
