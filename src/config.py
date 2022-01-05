import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    FOOBARTORY_ROBOTS = int(os.getenv("FOOBARTORY_ROBOTS", 2))


class ConfigLoader(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_configs()

    def load_configs(self):
        mapping = BaseConfig

        for k in dir(mapping):
            if k.isupper():
                self[k] = getattr(mapping, k)


config = ConfigLoader()
