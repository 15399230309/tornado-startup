from tornado.ioloop import IOLoop
from invoke import task

from startup.app import make_app


@task
def run(ctx, port=8000):
    app = make_app()
    app.listen(port)
    IOLoop.current().start()
