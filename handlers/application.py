#! -*- coding: utf-8 -*-

import tornado.web

class ApplicationHandler(tornado.web.RequestHandler):

  def get(self):
    self.render('base.html', test = 'init')

  def post(self):
    self.render('base.html', test = 'init')

  def _on_post(self):
    self.render('base.html', test = 'init')


