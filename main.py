from map_maker import maker
import time
import sys
import os

call_count = 0


def Block(sudoku, m, n):
    a = int(len(sudoku) ** .5)
    M = a * (m // a + 1)
    N = a * (n // a + 1)
    MM = max(0, M - a)
    NN = max(0, N - a)
    return list(map(lambda x: x[NN:N], sudoku[MM:M]))


def isValid(sudoku, m, n, v):
    a = sudoku[:]
    for i in a[m]:
        if i == v:
            return False
    for i in range(len(a)):
        if a[i][n] == v:
            return False
    T = ''.join(map(lambda x: ''.join(map(str, x)), Block(a, m, n))).replace('0', '')
    for i in T:
        if T.count(i) - 1:
            return False
    
    return True


def solver(su, Z=0, start: float = 0.0):
    global solved
    global file_name
    global call_count 
    solved = ''
    sudoku = su[:]
    AZ = 0
    for i in sudoku:
        AZ += i.count(0)
    bo = ""
    for i in sudoku:
        bo += '  '.join(map(str, i)) + "\n"

    os.system("cls")
    print(f"Function's call count: {call_count}\nSolved tile count: {Z}\nBoard's zero count: {AZ}\n{' ' * 6}====Board====\n{bo}" + "\n")
    call_count += 1
    m = Z // len(sudoku)
    n = Z % len(sudoku)
    
    if Z == len(sudoku) ** 2:
        os.system("cls")
        for i in sudoku:
            print('  '.join(map(str, i)))
            solved += '  '.join(map(str, i)) + '\n'
        file_name = board.replace('  ', '')[:9]
        with open("test_cases/solved_board/solved_board_" + file_name + ".board", 'w') as f:
            f.write(solved)
        times = round(time.time() - start, 3)
        print(f"solving took {times}sec")
        with open("test_cases/times/solving_time_" + file_name + ".board", 'w') as f:
            f.write(f"solving took {times}sec")
        sys.exit(Z)
    
    if sudoku[m][n]:
        solver(sudoku, Z + 1, start=start)
    else:
        for i in range(1, len(sudoku) + 1):
            if isValid(sudoku, m, n, i):
                sudoku[m][n] = i
                solver(sudoku, Z + 1, start=start)
                sudoku[m][n] = 0


def solving():
    global board
    global file_name
    valid = False
    board = ''
    while not valid:
        board = maker()
        try:
            board.replace("  ", "").index("000000000")
        except ValueError:
            valid = True
        else:
            pass
    file_name = board.replace('  ', '')[:9]
    with open("test_cases/unsolved_board/unsolved_board_" + file_name + ".board", 'w') as f:
        f.write(board)
    print(f"file_name:{file_name}")
    print("board:")
    print(board)
    print(f"zero count: {board.count('0')}")
    board = board.replace("  ", '')
    print("solved:")
    sudoku = list(map(lambda x: list(map(int, list(x))), board.split("\n")))
    solver(sudoku, start=time.time())


solving()
