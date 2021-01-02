# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# erro 1: valor padrão de funções mutável esperando-se que seja imutável

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# def foo(bar=[]):        # bar is optional and defaults to [] if not specified
#     bar.append("baz")    # but this line could be problematic, as we'll see...
#     return bar

# print(foo())
# print(foo())
# print(foo())

# # correção:
# def foo(bar=None):
#     if bar is None:		# or if not bar:
#         bar = []
#     bar.append("baz")
#     return bar

# print(foo())
# print(foo())
# print(foo())


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 2: esquecer-se de inicializar propriedades das classes filhas.

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# class A(object):
#     x = 1

# class B(A):
#     pass

# class C(A):
#     pass

# A.x = 3
# print (A.x, B.x, C.x)
# # espera-se que B.x = 1 e C.x = 1. Mas na verdade seus valores serão herdados de A, 
# # logo serão iguais a 3. Ao inicializar os valores das classes filhas, o problema é resolvido.


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 3: Escrita de lista de Exceptions incorretamente

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# try:
#     l = ["a", "b"]
#     int(l[2])
# except ValueError, IndexError:  # Expected to catch both exceptions, right?
#     pass

# O código acima dará erro tanto por ValueError quanto IndexError. Porém, o compilador não aceita passá-los 
# a não ser que seja por uma tupla (). Assim, com a correção fica:
# # except (ValueError, IndexError)


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 4: Erro de reconhecimento de escopo

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# x = 10
# def foo():
#     global x
#     x += 1
#     print(x)

# foo()

# # Acima ocorre um erro pois o escopo de x é considerado local, porém ele é global. 
# # Resolve-se isso ao declarar x como global. Ou seja, é feito o seguinte:

# x = 10
# def foo():
#     global x
#     x += 1
#     print(x)

# foo()

# # Mais um exemplo de erro ...

# lst = [1, 2, 3]
# def foo1():
#     lst.append(5)   # This works ok...
#     return lst

# print(foo1())

# lst = [1, 2, 3]
# def foo2():
#     lst += [5]      # ... but this bombs!
#     return lst

# print(foo2())

# # Ocorre um erro, pois em foo2() é feita uma inferência de que lst possui escopo local, 
# # pois em "lst = lst + [5]" é esperado que tal variável pertença a foo2(), o que não é o caso.


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 5: modificar uma lista enquanto iteramos ela

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# # Suponha que queiramos remover os números ímpares de uma lista de números de 0 a 9

# odd = lambda x : bool(x % 2)
# numbers = [n for n in range(10)]
# for i in range(len(numbers)):
#     if odd(numbers[i]):
#         del numbers[i]  # BAD: Deleting item from a list while iterating over it
# print(numbers)

# # O código acima resulta em erro pois o tamanho da lista é reduzido em tempo de execução,
# # resultando num IndexError. O problema acima é resolvido de maneira elegando com List Comprehension

# odd = lambda x : bool(x % 2)
# numbers = [n for n in range(10)]
# numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
# print(numbers)


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 6: Atribuição de valor numa closure

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# # Suponha que desejamos exibir a tabuada de um número escolhido. Podemos fazer o seguinte:
# def create_multipliers():
#     return [lambda x : i * x for i in range(1,11)]
# for multiplier in create_multipliers():
#     print(multiplier(2))

# Espera-se que o código acima retorne a tabuada do 2, porém ele usa apenas o último resultado de i
# para cada elemento da lista. Podemos resolver isso da maneira clássica:

# def create_multipliers(i):
#     lst = range(1,11)
#     for j in lst:
#         print(i * j)
# create_multipliers(3)

# # Porém, para resolver usando a solução apresentada inicialmente, basta fazer o seguinte:
# def create_multipliers():
#     return [lambda x, i=i : i * x for i in range(1,11)]

# for multiplier in create_multipliers():
#     print(multiplier(2))

# # Acima, temos iteramos por uma função anônima com dois argumentos (x e i), 
# # ao invés de um (como no primeiro caso). O valor padrão de i muda a cada iteração do laço implementado.
# # Assim obtemos o comportamente esperado. Ainda assim, prefiro a solução clássica neste caso.


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Erro 7: criação de referências circulares

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# # Ao tentar realizar este import, temos uma referência circular
# import b

# # basta realizarmos a mudança do import em b.py para dentro de g() para resolvermos o problema
# import b
# b.g()

