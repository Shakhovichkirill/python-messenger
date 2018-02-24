#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gbserver.server import Server
from gbcore.application import Application


if __name__ == "__main__":
    app = Application("config/env.json")
    app.logger.info("{} | Application start ...".format(__name__))

    server = Server(app)
    try:
        server.start()
    except KeyboardInterrupt:
        # Press Ctrl+C to stop
        pass
    finally:
        app.logger.info("{} | Application stop. Goodbye!".format(__name__))
