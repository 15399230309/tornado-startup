import os
from pathlib import Path

import yaml
from glom import glom, PathAccessError

ENV = os.environ.get('ENV') or 'dev'
ROOT: Path = Path(__file__).parent.parent


class Config:
    def __init__(self, env: str = 'dev'):
        self.env = env
        self.config_path = ROOT.joinpath(f'config/config-{env}.yml')
        with self.config_path.open(encoding='utf8') as yml:
            self.target = yaml.safe_load(yml)

    def get(self, option: str, default=None):
        return glom(self.target, option, default=default)

    def __getitem__(self, item):
        try:
            res = glom(self.target, item)
        except (PathAccessError, KeyError):
            raise KeyError(item)
        return res

    def reload(self):
        with self.config_path.open(encoding='utf8') as yml:
            self.target = yaml.safe_load(yml)


OPTIONS = Config(ENV)

if __name__ == '__main__':
    print(OPTIONS['web.port'])
