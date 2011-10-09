# -*- coding: utf-8 -*-
import os
import cherrypy

class Recipe:
  @cherrypy.expose
  def index(self):
    return "It's working"


cherrypy.quickstart(Recipe())
