# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos = ['Uno', 'Dos', 'Tres', 'Quatro', 'Cinco']

curso_teste = 'Teste'
curso_dos = 'Dos'
curso_cinco = 'Cinco'

notas = {}

if curso_teste in cursos:
  print(f'O curso {curso_teste} está na lista. Indique a avaliação:')
  notas[curso_teste] = int(input('De 0 a 20'))

if curso_dos in cursos:
  print(f'O curso {curso_dos} está na lista. Indique a avaliação:')
  notas[curso_dos] = int(input('De 0 a 20: '))

if curso_cinco in cursos:
  print(f'O curso {curso_cinco} está na lista. Indique a avaliação:')
  notas[curso_cinco] = int(input('De 0 a 20: '))

print(list(notas.values()))