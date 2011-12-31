# -*- coding: utf-8 -*-

import os, sys
import tornado.ioloop, tornado.web, tornado.httpserver
from app.config   import *
from app.handlers import *

def main():
  settings = {
    'static_path'   : os.path.join(os.path.dirname(__file__), "public"),
    'template_path' : os.path.join(os.path.dirname(__file__), "app/templates"),
    'debug': True
  }

  app = tornado.web.Application([
    (r'/', application.ApplicationHandler),
  ], **settings)

  port = int(os.environ.get("PORT", 5000))
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

# Initializing the application :-)
if __name__ == "__main__":
  main()
