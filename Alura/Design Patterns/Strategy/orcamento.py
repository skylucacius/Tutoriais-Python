# -*- coding: UTF-8 -*-
# orcamento.py
class Orcamento(object):
  def __init__(self, valor):
    self.__valor = valor

  @property
  def valor(self):
    return self.__valor