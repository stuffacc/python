import copy


# Здесь заполняем доску в зависимости от положения нового ферзя
# Доска, координаты ферзя
def fill_board(board, i_0, j_0):
    # Здесь нужна копия, чтобы не менялся основной список
    new_board = copy.deepcopy(board)
    
    # Поставить ферзя
    new_board[i_0][j_0] = 2
    count_empty = 0
    
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 2:
                continue
            # Ладья ходы
            if i == i_0 or j == j_0:
                new_board[i][j] = 1
            # Слон ходы
            if abs(i - i_0) == abs(j - j_0):
                new_board[i][j] = 1
            # Ладья + Слон = Ферзь


            # Количество пустых клеток
            if new_board[i][j] == 0:
                count_empty += 1

    return new_board, count_empty

# Доска, количество ферзей на доске, координаты начала
def recursion(board, count, start_i=-1, start_j=-1):
    # Если на доске N ферзей
    if count == len(board):
        # tuple, чтобы можно было добавить в set доску
        tuple_board = tuple(tuple(row) for row in board)
        a.add(tuple_board)
        return None

    # От каких координат начиннать
    if start_i != -1 and start_j != -1:
        new_board, count_empty = fill_board(board, start_i, start_j)

        # Идти дальше, если свободных мест >= чем осталось поставить ферзей
        if count_empty >= len(board) - (count + 1):
            recursion(board=new_board, count=count + 1)

        return None

    # Если координаты не передали, то первый попавшийся
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                # Если клетка пустая туда ферзя ставим
                if board[i][j] == 0:
                    new_board, count_empty = fill_board(board, i, j)
                    
                    # Идти дальше, если свободных мест >= чем осталось поставить ферзей
                    if count_empty >= len(board) - (count + 1):
                        recursion(board=new_board, count=count + 1)
                        
        return None

a = set()
n = int(input())

# Перебрать все начальные клетки
for i in range(n):
    for j in range(n):
        board = [[0 for _ in range(n)] for _ in range(n)]
        recursion(board=board, count=0, start_i=i, start_j=j)

print(len(a))

# 7 за 26 секунд
# 8 за 14 минут
