from random import sample


def maker():
    base = 3
    side = base * base
    
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side
    
    def shuffle(s):
        return sample(s, len(s))
    
    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))
    
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0
    
    num_size = len(str(side))
    sudoku_map = ''
    for line in board:
        sudoku_map += "" + "  ".join(f"{n or '0':{num_size}}" for n in line) + ""
        sudoku_map += "\n"
    return sudoku_map[:-1]
