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








# решение 2  -------- O(n!)


def is_valid(board, row, col):
    # Проверка наличия ферзя в данной строке
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Проверка по главной диагонали
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Проверка по побочной диагонали
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col):
    # Если все ферзи расставлены
    if col >= len(board):
        return 1
    
    count = 0
    for row in range(len(board)):
        if is_valid(board, row, col):
            # Расставление ферзя
            board[row][col] = 1
            
            # В следующий столбец
            count += solve_n_queens_util(board, col + 1)
            # Удаление ферзя
            board[row][col] = 0
            
    return count

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return solve_n_queens_util(board, 0)

print(solve_n_queens(n))

# Решение 3 ---------- O(1)

def solve_n_queens_constant(n):
    solutions = {
        1: 1,
        2: 0,
        3: 0,
        4: 2,
        5: 10,
        6: 4,
        7: 40,
        8: 92,
        9: 352,
        10: 724,
        11: 2680,
        12: 14200,
        13: 73712,
        14: 365596,
        15: 2279184,
        16: 14772512,
        17: 95815104,
        18: 666090624,
        19: 4968057848,
        20: 39029188884,
        21: 314666222712,
        22: 2691008701644,
        23: 24233937684440,
        24: 227514171973736,
        25: 2207893435808352,
        26: 22317699616364044,
        27: 234907967154122528
}
    return solutions.get(n, 0)

print(solve_n_queens_constant(n))


