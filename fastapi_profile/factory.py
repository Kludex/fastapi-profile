from fastapi_profile.custom_route import ProfileRoute


# prefer arguments (duck typing)
def ProfilerRouteFactory(config):
    return ProfileRoute
