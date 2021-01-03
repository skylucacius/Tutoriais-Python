# A Narcissistic Number is a positive number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. In this Kata, 
# we will restrict ourselves to decimal (base 10).

# The Challenge:

# Your code must return true or false depending upon whether the given number is 
# a Narcissistic number in base 10. Error checking for text strings or other invalid inputs is 
# not required, only valid positive non-zero integers will be passed into the function.
# import math
# def narcissistic( n ):
#     qtdCasas = 0 if n == 0 else math.floor(1 + math.log10(n))
#     soma = 0
#     # somaDecimal = 0
#     digito = 0
#     somaNarcisistica = 0
#     i = 0
#     for i in range(1,qtdCasas):
#         # valor = (n % 10**i - digito)
#         digito = int((n % 10**i - digito) / (10**(i-1)))
#         # soma += valor
#         # somaDecimal += digito * (10**(i-1))
#         somaNarcisistica += digito ** (qtdCasas)
#         # print(digito)
#     # ultimoValor = (n - soma)
#     ultimoDigito = int((n - soma) / (10**i))
#     # somaDecimal += ultimoDigito * (10**i)
#     somaNarcisistica += ultimoDigito ** (qtdCasas)
#     # print(ultimoDigito)
#     # soma += ultimoValor
#     # print(soma)
#     # print(somaDecimal)
#     # print(somaNarcisistica)
#     return somaNarcisistica == n




# # usado para responder no SO
# import math
# def narcissistic( n ):
#     DecimalPlaces = 0 if n == 0 else math.floor(1 + math.log10(n))
#     soma = 0
#     digit = 0
#     NarcissisticSum = 0
#     i = 0
#     for i in range(1,DecimalPlaces):
#         digit = int((n % 10**i - digit) / (10**(i-1)))
#         NarcissisticSum += digit ** (DecimalPlaces)
#     lastDigit = int((n - soma) / (10**i))
#     NarcissisticSum += lastDigit ** (DecimalPlaces)
#     return NarcissisticSum == n

# print(narcissistic(0o001)) # deve retornar true
# print(narcissistic(153)) # deve retornar true
# print(narcissistic(1938)) # deve retornar false
