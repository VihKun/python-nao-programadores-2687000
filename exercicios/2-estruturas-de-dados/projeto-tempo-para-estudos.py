# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

# 1:
nome = input('Por favor, introduza o nome do estudante:')

# 2:
total_dias = input('Por favor, introduza o total de dias dedicados ao estudo por semana:')

# 3:
total_horas = input('Por favor, introduza a média de horas de estudo por dia:')

# 4:
curso = input('Por favor, introduza o nome do curso:')

# 5:
total_dias = int(total_dias)
total_horas = int(total_horas)

print(f'O/A estudante {nome} dedica {total_dias} dias por semana aos estudos, estudando em média {total_dias * total_horas} horas por semana, no curso de {curso}.')