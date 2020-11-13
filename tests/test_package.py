from importlib import util


def test_package():
    fastapi_profile_spec = util.find_spec("fastapi_profile")
    assert fastapi_profile_spec is not None
