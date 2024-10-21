# Declare 4 variáveis do tipo numérica
x = 2
y = 3
z = 7
a = 4

# Crie uma estrutura condicional para comparar dois números
comparacao = True
if x > y:
  print(f'O número {x} é maior que {y}.')
else:
  print(f'O número {x} é menor que {y}.')

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if y < z:
  print(f'A condição foi cumprida e o número de maior valor é o {z}.')

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if a > z:
  print('Erro')
else:
  print(f'A condição é negativa e o número de maior valor é {z}.')

# Insira outras condições na estrutura condicional usando o elif
if a > z:
  print('Erro')
elif a < z:
  print('Verdadeiro')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if a > z or y < z:
  print('Uma das condições é verdadeira.')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"
if a < z:
  print('Verdadeiro')
if y < z:
  print('Verdadeiro')