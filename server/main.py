import sys
import signal
import logging
from host import Host

def main():
     # Set exit handler
    set_exit_handler(on_exit)

    # setup loggin
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )


    # Create objects
    host = Host()
    host.start_server(8080)

# Define Exit handler
def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)

def on_exit(sig, func=None):
    logging.info("Shutting down")
    sys.exit(0)

# Main
if __name__ == "__main__":
    main()