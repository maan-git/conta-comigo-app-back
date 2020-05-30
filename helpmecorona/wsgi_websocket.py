# import os
# import gevent.socket
# import redis.connection
# redis.connection.socket = gevent.socket
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpmecorona.settings.dev")
# from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
# application = uWSGIWebsocketServer()

import os
# import sys
import logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helpmecorona.settings.dev")

from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

_websocket_app = uWSGIWebsocketServer()


def application(environ, start_response):
    logging.info('########################## Connection ########################################')
    return _websocket_app(environ, start_response)
