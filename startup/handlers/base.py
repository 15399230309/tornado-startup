from typing import Union

from aiopg.sa import create_engine
from tornado.web import RequestHandler

from startup import OPTIONS


class BaseHandler(RequestHandler):

    def data_received(self, chunk: bytes):
        pass

    def initialize(self) -> None:
        self.engine = create_engine(
            host=OPTIONS['pg.host'],
            port=OPTIONS['pg.port'],
            database=OPTIONS['pg.dbname'],
            user=OPTIONS['pg.user'],
            password=OPTIONS['pg.pwd']
        )
        self.conn = None

    async def prepare(self):
        self.engine = await self.engine
        self.conn = await self.engine.acquire()

    def finish(self, chunk: Union[str, bytes, dict] = None):
        self.conn.close()
        self.engine.close()
        super().finish(chunk)
