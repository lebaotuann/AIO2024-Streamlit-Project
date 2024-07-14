import os

DATA_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_DIRECTORY_PATH.replace("\\", "/")  # No slash character at the path's end.
