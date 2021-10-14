from map_maker import maker
import time
import sys
import os
from matplotlib import pyplot as plt

call_count = 1
debug = False
values = []


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


def solver(su, Z=0, start: float = 1.0, debug=False):
    global values
    global solved
    global file_name
    global call_count
    global boa
    AZ, bo = [0, ""]
    solved = ''
    sudoku = su[:]
    star = time.time()
    try:
        values.append(call_count / (star - start))
    except ZeroDivisionError:
        values.append(0)
    if debug:
        os.system("cls")
        AZ = 0
        for i in sudoku:
            AZ += i.count(0)
        bo = ""
        for i in sudoku:
            bo += '  '.join(map(str, i)) + "\n"
        print(f"①: File name: {file_name}")
        print(f"②: Z count(numbers that solved with function, If it is 81, the board is solved.): {Z}")
        print(f"③: Function's call count: {call_count}")
        print(f"④: Time spend: {round(star - start, 3)}")
        print("The higher the value of 5, the higher the efficiency.")
        try:
            print(f"⑤: Call count / spend time ratio: {call_count / (star - start)}")
        except ZeroDivisionError:
            print(f"⑤: Call count / spend time ratio: {0}")
        print(f"⑦: Solved tile count: {81 - AZ}")
        print(f"⑧: Board's zero count: {AZ}")
        print("==========Board==========")
        print(bo[:-1])
        print("==========board==========")
        print(boa)
    call_count += 1
    m = Z // len(sudoku)
    n = Z % len(sudoku)
    
    if Z == len(sudoku) ** 2:
        os.system("cls")
        for i in sudoku:
            solved += '  '.join(map(str, i)) + '\n'
        file_name = board.replace('  ', '')[:9]
        with open("test_cases/solved_board/solved_board_" + file_name + ".board", 'w') as f:
            f.write(solved)
        times = round(time.time() - start, 3)
        star = time.time()
        print(f"①: File name: {file_name}")
        print(f"②: Z count(numbers that solved with function, If it is 81, the board is solved.): {Z}")
        print(f"③: Function's call count: {call_count}")
        print(f"④: Time spend: {round(star - start, 3)}")
        print("The higher the value of 5, the higher the efficiency.")
        print(f"⑤: Call count / spend time ratio: {call_count / (star - start)}")
        print(f"⑦: Solved tile count: {81 - AZ}")
        print(f"⑧: Board's zero count: {AZ}")
        print("==========Board==========")
        print(bo[:-1])
        print("==========board==========")
        print(boa)
        x = [x for x in range(call_count - 1)]
        plt.plot(x, values, 'b')
        plt.show()

        with open("test_cases/times/solving_time_" + file_name + ".board", 'w') as f:
            f.write(f"solving took {times}sec")
        sys.exit(Z)
    
    if sudoku[m][n]:
        solver(sudoku, Z + 1, start, debug)
    else:
        for i in range(1, len(sudoku) + 1):
            if isValid(sudoku, m, n, i):
                sudoku[m][n] = i
                solver(sudoku, Z + 1, start, debug)
                sudoku[m][n] = 0


if __name__ == '__main__':
    valid = False
    board = ''
    boa = ''
    os.system("cls")
    while not valid:
        board = maker()
        try:
            board.replace("  ", "").index("000000000")
        except ValueError:
            boa = board
            valid = True
        else:
            pass
    if "-print" in sys.argv:
        debug = True
    else:
        debug = False
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
    solver(sudoku, 1, time.time(), debug)
