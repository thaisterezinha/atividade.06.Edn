import random
import string

# Conjunto de caracteres disponíveis
letras = string.ascii_letters   # A-Z e a-z
numeros = string.digits         # 0-9
simbolos = string.punctuation   # !@#$%&*()_+= etc.

# Combina todos os tipos de caracteres
caracteres = letras + numeros + simbolos

# Solicita ao usuário o comprimento da senha
tamanho = int(input("Quantos caracteres você deseja na senha? "))

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

# Exibe a senha gerada
print(f"Senha gerada: {senha}")
