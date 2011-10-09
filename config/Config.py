#! -*- coding: utf-8 -*-

# Here you can set up your environment variables, static path, and other.
# While in production, debug should be False.

import os

class Config:

  def settings(dictn = {}):
    """ Define settings """

    settings = {
      'static_path'   : os.path.join(os.path.dirname(__file__), "static"),
      'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
      'debug': True
    }
    if len(dictn) > 0:
      settings.append(dictn)

