import os

def load_env_variable(key, default=None):
    return os.getenv(key, default)
