# Exemplos e exercícios do livro Pense em Python
# pg 35

mensagem = "Estudando variáveis em Python"
pi = 3.14159265
x = round(pi, 4)
print(x)
print(len(mensagem))

# Instrução import
import math # importa o módulo math (variáveis e funções matemáticas)
num = math.pow(5, 2) # função potenciação, eleva o primeiro ao segundo
#num = 5 ** 3
print(num)
print(math.sqrt(num)) # função sqrt calcula a raiz quadrada
print('O valor de pi com 15 casas decimais é', math.pi)

# Argumentos
print(int('302', 4)) # o segundo argumento de int define a base do primeiro argumento
print(float('123.23')) #float só permite um argumento
