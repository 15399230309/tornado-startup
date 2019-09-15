import importlib

from startup import ROOT

__all__ = ['user']


class Route:
    __handlers = {}

    def __init__(self, app, prefix='/api/v1'):
        self.app = app
        self.__handlers.setdefault(self.app, [])
        self.prefix = prefix

    @property
    def handlers(self):
        handlers = ROOT.joinpath('startup/handlers').glob("*.py")
        for handler in handlers:
            if handler.name.startswith('__'):
                continue
            importlib.import_module(
                f"startup.handlers.{handler.name.rstrip('.py')}")
        # pylint: disable=protected-access
        return self.__class__.__handlers[self.app]

    def __call__(self, endpoint):
        def decorator(handler):
            uri = f'{self.prefix}{endpoint}'
            route_url = uri, handler
            self.__handlers[self.app].append(route_url)

        return decorator

    @classmethod
    def get_handlers(cls):
        return [handler for handler in cls.__handlers.values()]


user = Route('user')
