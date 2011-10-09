#! -*- coding: utf-8 -*-

import application

class RecipeHandler(application.ApplicationHandler):

  def get(self):
    self.render('base.html', test = 'working?')


class FindRecipeHandler(RecipeHandler):
  """Find the recipes by the parameter"""

  def get(self):
    self.render('base.html', test = self.get_argument("recipe"))
