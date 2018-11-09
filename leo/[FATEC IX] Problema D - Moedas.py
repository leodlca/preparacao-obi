n_of_lines = int(input())

cambios = []

for i in range(0, n_of_lines):
  input_raw = input().split(" ")
  moeda = input_raw[0]
  valor = float(input_raw[1])
  cambios.append({"moeda": moeda, "valor": valor})
  
valor_necessario = float(input())

resultado = []

for cambio in cambios:
  resultado.append({"valor": (valor_necessario * 100) / cambio['valor'], "moeda": cambio['moeda']})
  
for cambio_res in resultado:
  print(cambio_res['moeda'] + ' ' + '%.2f' % cambio_res['valor'])
