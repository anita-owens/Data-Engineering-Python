import os

def env_vars():
    return os.environ.get('FOO', 'Specified environment variable is not set.')

env_vars()