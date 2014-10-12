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
from host import Host

# Definitions
app = None
logger = None
host = None

def main():

    # Globals
    global logger, app, host

     # Set exit handler
    set_exit_handler(on_exit)

    # Create objects
    host = Host()
    logger = Log().instance()

    logger.info("Server is ready!")

    host.start_server(8080)

# Define Exit handler
def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)

def on_exit(sig, func=None):
    sys.exit(0)

# Main
if __name__ == "__main__":
    main()