# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

# 1:
nome = input("Introduza o seu nome:")
ano = input("Introduza o ano em que conheceu o LinkedIn:")
ano_atual = input("Introduza o ano atual:")
cursos = input("Introduza os cursos realizados no LinkedIn Learning separados por vírgula e em ordem cronológica:")

# 2:
cursos = cursos.split(', ')
anos_total = int(ano_atual) - int(ano)
cursos_num = len(cursos)
pessoa = {
  'nome' : nome,
  'ano' : ano,
  'ano_atual' : ano_atual,
  'cursos' : cursos
}

# 3:
print(f"O seu nome é {pessoa['nome']} e conheceu o LinkedIn no ano {pessoa['ano']}. Desde então, {anos_total} anos se passaram, tendo sido realizados {cursos_num} cursos, sendo o primeiro {pessoa['cursos'][0]} e o último {pessoa['cursos'][cursos_num - 1]}.")