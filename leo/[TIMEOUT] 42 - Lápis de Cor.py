# +- 1h30min, 60/100 pontos, TIMEOUT (mais de 1000ms) em 12 de 40 casos.
# Complexidade exponencial de O(n^4) no pior caso, por isso nos testes grandes, recebo erro de timeout.

# Uma otimização geral foi tornar a lista "square" e o n_of_sides locais em todas as funções em que 
# ela é acessada, pq é dito na documentação do python que variáveis locais são sempre
# de mais fácil e rápido acesso do que as globais
    
# Aqui é que acontece a seleção de quem pode ser pintado ou não, otimizei
# todas as operações matemáticas colocando-as dentro de variáveis, e reduzindo
# o worst-case cenário de todos os ifs que consegui.
# No melhor caso, cada iteração do loop de baixo passa por 4 ifs, no pior passa por 46 ifs aqui dentro.
def paint_n_level(row, column, level, square, n_of_sides):

    str_level = str(level)
    level_minus_one = level - 1
    
    # Pinta a row mais alta
    if row > (level_minus_one):
        paint_item(row-(level), column, str_level, square)

    # Pinta a row mais baixa
    if row < (n_of_sides - level):
        paint_item(row+level, column, str_level, square)

    for i in range(0, level_minus_one):

        column_comparator = level_minus_one - i
        i_plus_1 = i + 1

        # Pinta as rows intermediárias de cima
        if row > i:
            if column >= column_comparator:
                paint_item(row - i_plus_1, column - column_comparator , str_level, square)
            if column < n_of_sides - column_comparator:
                paint_item(row - i_plus_1, column + column_comparator, str_level, square)

        # Pinta as rows intermediárias de baixo
        if row < n_of_sides - (i_plus_1):
            if column >= column_comparator:
                paint_item(row + i_plus_1, column - column_comparator, str_level, square)
            if column < n_of_sides - column_comparator:
                paint_item(row + i_plus_1, column + column_comparator, str_level, square)

    # Pinta a própria row
    if column >= level:
        paint_item(row, column-level, str_level, square)
    if column < (n_of_sides - level):
        paint_item(row, column+level, str_level, square)

# Não pensei em nada pra otimizar esse.
def paint_item(row, column, content, square):
    if square[row][column] == '*' or int(square[row][column]) > int(content): square[row][column] = content

# Já otimizei esse loop trocando os forEach por ranges e adicionando as variáveis globais aqui.
def correct_painting():
    n_of_sides = int(input(""))
    square = []

    for i in range(0, n_of_sides):
        square.append(list(input("")))

    for row_index in range(0, n_of_sides):
        for column_index in range(0, n_of_sides):
            if square[row_index][column_index] == '0':
                for level in range(1, 10):
                    paint_n_level(row_index, column_index, level, square, n_of_sides)

    return [square, n_of_sides]

# Otimizei esse do mesmo jeito do anterior e botando o print de carona, eliminando um loop.
def paint_9_all_over_it(square, n_of_sides):
    for row_index in range(0, n_of_sides):
        for column_index in range(0, n_of_sides):
            if square[row_index][column_index] == '*':
                square[row_index][column_index] = '9'
        print(''.join(square[row_index])) # Coloquei esse print aqui pegando carona no último loop executado pelo programa.

res = correct_painting()
paint_9_all_over_it(res[0], res[1])