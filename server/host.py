import bottle
from bottle import redirect, static_file
from limewsadapter import LimeWSAdapter
from datacache import DataCache
import os
import sys
import os.path
import logging
import signal
from customlogger import Log

class Host:

    # Definitions
    app = None,
    logger = None
    dataCahce = None

    def __init__(self):
        global app, logger, dataCache

        # Create objects
        app = bottle.app()
        logger = Log().instance()
        dataCache = DataCache()

        # Init
        dataCache.refresh()

    # Start server
    def start_server(port):
        global  app

        # Ready to serve
        logger.info("Server is starting")
        bottle.run(host="0.0.0.0", port=int(port), app=app, server='cherrypy', debug=True, reloader=True)

    # Index page
    @app.route('/')
    def send_static(self):
        return static_file('/index.html', root='../client/app/')

    # GetTastings
    @app.route('/api/tastings/', method='GET')
    def getTastings(self):
       print("Get all tastings with drinks")

    # GetDrinks
    @app.route('/api/drinks/', method='GET')
    def getDrinks(self):
       print("Get all drunks")

    # PutReview
    @app.route('/api/review/', method='PUT')
    def putReview(self):
       print("Save review")

    # Static content
    @app.route('/client/<filename:path>')
    def send_static(filename):
        filename = filename
        if os.path.isfile('../client/app/'+filename):
            return static_file(filename, root='../client/app/')
        return ''
