n_of_lines = int(input())

lista_de_parenteses = []

for i in range(0, n_of_lines):
  lista_de_parenteses.append(input())

for string_parenteses in lista_de_parenteses:
  parenteses_char = list(string_parenteses)
  incorrect = False
  contador = 0
  for caractere in parenteses_char:
    if caractere == '(': 
      contador += 1
    else:
      contador -= 1
    if contador < 0:
      incorrect = True
      break
  if incorrect or contador != 0:
    print('falso')
  else:
    print('verdadeiro')