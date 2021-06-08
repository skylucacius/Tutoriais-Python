# -*- coding: UTF-8 -*-

class Calculador_de_impostos(object):

  def realiza_calculo(self, orcamento, imposto):

      print(imposto(orcamento))

if __name__ == '__main__':
    from orcamento import Orcamento
    from impostos import calcula_ICMS, calcula_ISS

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    # ISS é 6% do orçamento e ICMS é 10% do orçamento
    calculador_de_impostos.realiza_calculo(orcamento, calcula_ISS) ## exibirá 30
    calculador_de_impostos.realiza_calculo(orcamento, calcula_ICMS) ## exibirá 50
