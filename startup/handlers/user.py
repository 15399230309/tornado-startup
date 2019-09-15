from startup.handlers import route
from startup.handlers.base import BaseHandler


@route.user(r'/login')
class LoginHandler(BaseHandler):
    async def get(self, *args, **kwargs):
        res = await self.conn.execute("select 1, pg_sleep(1)")
        async for row in res:
            self.write(str(row[0]).encode())
