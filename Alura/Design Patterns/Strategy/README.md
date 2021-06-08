# Design Pattern Strategy

Ele se encarrega de utilizar o paradigma funcional para resolver o problema de múltiplos ifs. O exercício implementado aqui visa resolver esse problema através do paradigma funcional. Também é possível resolvê-lo utilizando o paradigma OO com o Duck Typing do Python.

Basicamente, se houver uma série de ifs, ou um switch, a decisão de qual bloco de código a ser executado será resolvido por meio de funções: a chamada do método em que será implementado o Strategy deverá conter uma função (como se fosse um enum) para a escolha de qual bloco de código executar.