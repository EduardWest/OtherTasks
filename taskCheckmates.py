# Задача по шахматам
class CheckException(Exception):
    pass

def testfigure(x1, y1, x2, y2, x3, y3): # (x1, y1) - координаты белой дальи, (x2, y2) - координаты белого короля, (x3, y3) - координаты черного короля
    while True:
        if type(x1) != int or type(x2) != int or type(x3) != int  or type(y1) != int or type(y2) != int or type(y2) != int or type(y3) != int:
            print('Error: В координатах не должно быть дробных чисел и/или букв!! Повторите ввод')
            while True:
                try:
                    x1 = int(input())
                    y1 = int(input())
                    x2 = int(input())
                    y2 = int(input())
                    x3 = int(input())
                    y3 = int(input())
                    break
                except ValueError:
                    print('Error: В координатах не должно быть дробных чисел и/или букв!! Повторите ввод')
            continue
        if ((x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3)) and (x1 not in range(1, 9) or x2 not in range(1, 9) or x3 not in range(1, 9) or y1 not in range(1, 9) or y2 not in range(1, 9) or y3 not in range(1, 9)):
            print('Error: Две или более фигуры находятся в одной клетке. \n'+'Error: Для одной или более фигур недопустимые координтаты.Повторите ввод')
            while True:
                try:
                    x1 = int(input())
                    y1 = int(input())
                    x2 = int(input())
                    y2 = int(input())
                    x3 = int(input())
                    y3 = int(input())
                    break
                except ValueError:
                    print('Error: В координатах не должно быть дробных чисел и/или букв!! Повторите ввод')

            continue
        if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
            print('Error: Две или более фигуры находятся в одной клетке. Повторите ввод')
            while True:
                try:
                    x1 = int(input())
                    y1 = int(input())
                    x2 = int(input())
                    y2 = int(input())
                    x3 = int(input())
                    y3 = int(input())
                    break
                except ValueError:
                    print('Error: В координатах не должно быть дробных чисел и/или букв!! Повторите ввод')
            continue
        if x1 not in range(1, 9) or x2 not in range(1, 9) or x3 not in range(1, 9) or y1 not in range(1, 9) or y2 not in range(1, 9) or y3 not in range(1, 9):
            print('Error: Для одной или более фигур недопустимые координтаты. Повторите ввод')
            while True:
                try:
                    x1 = int(input())
                    y1 = int(input())
                    x2 = int(input())
                    y2 = int(input())
                    x3 = int(input())
                    y3 = int(input())
                    break
                except ValueError:
                    print('Error: В координатах не должно быть дробных чисел и/или букв!! Повторите ввод')
            continue
        else:
            break
    if (y2 == y3 and (x2 == x3 - 1 or x2 == x3 + 1)) or (x2 == x3 and (y2 == y3 - 1 or y2 == y3 + 1)) or ((x2 == x3 + 1 or x2 == x3 -1) and (y2 == y3 + 1 or y2 == y3 - 1)):
        return('Strange')
    elif (y3 != y1 and x3 != x1):
        if x3 == 1 and y3 == 1:
            if x1 == 2 and y1 == 2 and abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
                return('Stalemate')
            else:
                return('Normal')
        elif x3 == 1 and y3 == 8:
            if x1 == 2 and y1 == 7 and abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
                return('Stalemate')
            else:
                return('Normal')
        elif x3 == 8 and y3 == 8:
            if x1 == 7 and y1 == 7 and abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
                return('Stalemate')
            else:
                return('Normal')
        elif x3 == 8 and y3 == 1:
            if x1 == 7 and y1 == 2 and abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1:
                return('Stalemate')
            else:
                return('Normal')
        else:
            return('Normal')
    elif x3 == x1 or y3 == y1:
        if x3 == x1 and x3 == x2 and ((y1 > y2 > y3) or (y3 > y2  > y1)):
            return('Normal')
        elif y3 == y1 and y3 == y2 and ((x1 > x2 > x3) or (x3 > x2  > x1)):
            return('Normal')
        elif  not (x3 == x1 and x3 == x2 and ((y1 > y2 > y3) or (y3 > y2  > y1))) or (y3 == y1 and y3 == y2 and ((x1 > x2 > x3) or (x3 > x2  > x1))):
            if (y3 == 1 and  x3 == 1) or (y3 == 1 and x3 == 8) or (y3 == 8 and x3 == 1) or (y3 == 8 and x3 == 8):
                if ((y3 == y2 or abs(y3 - y2) == 1) and abs(x2 - x3) == 2 and x3 == x1 and abs (y1 - y3) >= 2) or ((x3 == x2 or abs(x3 - x2) == 1) and abs(y2 - y3) == 2 and y3 == y1 and abs (x1 - x3) >= 2):
                    return('Checkmate')
                else:
                    return('Check')
            if y3 == 1 or y3 == 8:
                if (x2 == x3 and abs(y3 - y2) == 2) and (y3 == y1 and abs(x3 - x1) >= 2):
                    return('Checkmate')
                else:
                    return('Check')
            elif x3 == 1 or x3 == 8:
                if (y2 == y3 and abs(x3 - x2) == 2) and (x3 == x1 and abs(y3 - y1) >= 2):
                    return('Checkmate')
                else:
                    return('Check')
            else:
                return('Check')
        else:
            return('Check')
results = []        
for i in range(1,9): # i,j - белая ладья, k,f - белый король, h,t - черный король
    for j in range(1,9):
        for k in range(1,9):
            for f in range(1,9):
                for h in range(1,9):
                    for t in range(1,9):
                         if (i == k and j == f) or (i == h and j == t) or (k == h and f == t):
                             continue
                         else:
                             results.append(testfigure(i, j, k, f, h, t))
                             
                             
                             
  
print(len(results),results.count('Normal'), results.count('Strange'), results.count('Check'), results.count('Checkmate'), results.count('Stalemate'), sep ='\n')
print(len(results) == results.count('Normal') + results.count('Strange') + results.count('Check') + results.count('Checkmate') + results.count('Stalemate'))
