#! -*- coding: utf-8 -*-

import tornado.web

class ApplicationHandler(tornado.web.RequestHandler):

  # while in GET events
  def get(self):
    self.render('base.html', test = 'Hello world')

  # while in POST events
  def post(self):
    self.render('base.html', test = 'Hello post world :O')

  # On post event :O
  def _on_post(self):
    self.render('base.html', test = 'This is real!')


