import logging

from tornado.web import Application

from startup import OPTIONS
from startup.http.route import user


class StartupApp(Application):

    def __init__(self):
        logging.info("start app")
        handlers = user.handlers

        settings = {
            'compiled_template_cache': False,
            'serve_traceback': True,
            'xsrf_cookies': False,
            "cookie_secret": "",
        }
        Application.__init__(
            self, handlers, debug=OPTIONS["debug"], **settings)


def make_app():
    app = StartupApp()
    return app
