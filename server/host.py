from bottle import redirect, static_file, Bottle, request
from limewsadapter import LimeWSAdapter
import os
import os.path
import logging

class Host:

    def __init__(self):

        # Create objects
        self._app = Bottle()
        self._route()

    def _route(self):

        self._app.route('/', method="GET", callback=self._send_main_page)
        self._app.route('/<filename:path:re:^(?!/api).+>', method="GET", callback=self._send_static)

        self._app.route('/api/event/', method="GET", callback=self._get_events)
        self._app.route('/api/whisky/', method="GET", callback=self._get_whisky)
        self._app.route('/api/user/', method="GET", callback=self._get_users)
        self._app.route('/api/review/', method="POST", callback=self._post_review)

    # Start server
    def start_server(self, port):

        # Ready to serve
        logging.info("Server is starting")
        self._app.run(host="0.0.0.0", port=int(port), server='cherrypy', debug=True, reloader=True)

    @staticmethod
    def _send_main_page():
        return static_file('/index.html', root='../client/app/')

    @staticmethod
    def _send_static(filename):
        if os.path.isfile('../client/app/'+filename):
            return static_file(filename, root='../client/app/')
        else:
            logging.warning("static file not found: %s" % filename)
        return ''

    @staticmethod
    def _get_events():
        return LimeWSAdapter.get_events()
        return Host.jsonp(request, LimeWSAdapter.get_events())

    @staticmethod
    def _get_whisky():
        event = request.query.get('event')
        return Host.jsonp(request, LimeWSAdapter.get_whisky_by_event(event))

    @staticmethod
    def _get_users():
        event = request.query.get('event')
        return Host.jsonp(request, LimeWSAdapter.get_users(event))

    @staticmethod
    def _post_review():
        content = request.json
        print(content)
        return LimeWSAdapter.add_review(content)

    @staticmethod
    def jsonp(request, dictionary):
        if request.query.callback:
            return "%s(%s)" % (request.query.callback, dictionary)
        return dictionary


