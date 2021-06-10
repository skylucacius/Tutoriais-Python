# Design Pattern Template Method

Usa-se este padrão quando houver um padrão a ser seguida para diferentes regras.

No exemplo implementado aqui, devem ser aplicados diferentes impostos seguindo uma mesma estrutura: ou aplica-se a máxima ou a mínima taxação. A regra a ser seguida está numa classe abstrata, e as classes que a seguem devem implementar os métodos abstratos que compõem tal regra.