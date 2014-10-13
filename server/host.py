import bottle
from bottle import redirect, static_file, Bottle
from limewsadapter import LimeWSAdapter
from datacache import DataCache
import os
import sys
import os.path
import logging
import signal
from customlogger import Log


class Host:

    def __init__(self):

        # Create objects
        # app = bottle.app()
        self.logger = Log().instance()
        self.dataCache = DataCache()

        self._app = Bottle()
        self._route()

        # Init
        self.dataCache.refresh()

    def _route(self):
        self._app.route('/', method="GET", callback=self._sendMainPage)
        self._app.route('/client/<filename:path>', method="GET", callback=self._send_static)

        self._app.route('/api/tasting/', method="GET", callback=self._getTastings)
        self._app.route('/api/drink/', method="GET", callback=self._getDrinks)
        self._app.route('/api/user/', method="GET", callback=self._getUsers)

        self._app.route('/api/review/', method="PUT", callback=self._putReview)

    # Start server
    def start_server(self, port):

        # Ready to serve
        self.logger.info("Server is starting")
        self._app.run(host="0.0.0.0", port=int(port), server='cherrypy', debug=True, reloader=True)

    def _sendMainPage(self):
        return static_file('/index.html', root='../client/app/')

    def _getTastings(self):
        return LimeWSAdapter.get_tastings()

    def _getDrinks(self):
       print("Get all drunks")

    def _getUsers(self):
       print("Get all drunks")

    def _putReview(self):
       print("Save review")

    def _send_static(filename):
        filename = filename
        if os.path.isfile('../client/app/'+filename):
            return static_file(filename, root='../client/app/')
        return ''
