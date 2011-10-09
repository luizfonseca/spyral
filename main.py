# -*- coding: utf-8 -*-
import os, sys
import tornado.ioloop
import tornado.web
import tornado.httpserver
from handlers import *

def main():
  settings = {
    'static_path'   : os.path.join(os.path.dirname(__file__), "static"),
    'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    'debug': True
  }

  app = tornado.web.Application([
    (r'/', application.ApplicationHandler),
    (r'/recipe', recipe.RecipeHandler),
    (r'/find', recipe.FindRecipeHandler)
  ], **settings)

  port = int(os.environ.get("PORT", 5000))
  http_server = tornado.httpserver.HTTPServer(app)
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()

# Initializing the application :-)
if __name__ == "__main__":
  main()
