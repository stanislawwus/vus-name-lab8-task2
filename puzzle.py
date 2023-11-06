"""
Function for validating game boards
https://github.com/stanislawwus/vus-name-lab8-task2.git
"""
def validate_board(board: list[str]) -> bool:
    """
    Function to check whether the board is correct
    >>> check(["**** ****", "***1 ****", "**  3****", \
"* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    board = [list(i) for i in board]
    for  i in board:
        for j in i:
            if j.isdigit() and i.count(j)>1:
                return False
    board_y = [[i[j] for i in board] for j in range(9)]
    for  i in board_y:
        for j in i:
            if j.isdigit() and i.count(j)>1:
                return False
    blocks = []
    for i in range(5):
        block = []
        for elem in board:
            if elem[i] != '*':
                block.append(elem[i])
        blocks.append(block)
    for row in blocks:
        while len(row) > 4:
            row.pop(len(row)-1)
    board = [[j for j in i if j != '*']for i in board]
    for row in board:
        while len(row) > 5:
            row.pop(0)
    for i in range(5):
        blocks[i].extend(board[8-i])
    for j in blocks:
        for elem in j:
            if elem.isdigit() and j.count(elem)>1:
                return False
    return True
