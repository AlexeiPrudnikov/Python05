import random
def PrintSquare(square):
    for i in square:
        print(' '.join(i))
def IsWin(square):
    for i in square:
        if i == ['X','X','X'] or i == ['0','0','0']:
            return True
    if ((square[0][0] == square[1][1] == square[2][2]) or (square[0][2] == square[1][1] == square[2][0])) and not (square[1][1] == ' '):
        return True
    for i in range(3):
        if (square[0][i] == square[1][i] == square[2][i]) and not (square[0][i] == ' '):
            return True
    return False
def GetStep (i, square):
    while (True):
        x = int(input(f'{i + 1}-й игрок введите номер строки:'))
        y = int(input(f'{i + 1}-й игрок введите номер столбца:'))
        if (0 <= x <= 2) and (0 <= y <= 2) and (square[x][y] == ' '):
            if i:
                square[x][y] = 'X'
            else:
                square[x][y] = '0'
            return square
        else:
            print('Недопустимый ход, повторите ввод.')
square = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print('Происходит жеребьевка...')
first = random.randint(1, 2)
flag = bool(first - 1)
print(f'Ходит первым {first}-й игрок')
notWin = True
while not(IsWin(square)):
    square = GetStep(int(flag), square)
    PrintSquare(square)
    notWin = not (IsWin(square))
    if not(notWin):
        print(f'{int(flag) + 1}-й игрок победил!')
    flag = not flag
