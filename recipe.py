# -*- coding: utf-8 -*-
import os
import cherrypy
import urllib




class Recipe:
  @cherrypy.expose
  def index(self):
    return "Natasha <3"


cherrypy.quickstart(Recipe())
