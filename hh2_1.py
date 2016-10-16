#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    k = int(input())
    answer=[]
    for i in range(k):
        n, m = list(map(int,input().split()))
        mas = [[int(j) for j in input().split()] for i in range(n)] 
        d,sum1,sum2 = [],0,0
        for i in mas:
            sum1+=sum(i)
        for i in range(len(mas)):
            for j in range(len(mas[i])):
                if i!=0 and j!=0 and i!=n-1 and j!=m-1:
                    if mas[i][j] >= max(mas[i][j+1], mas[i][j-1], mas[i+1][j], mas[i-1][j]):
                        if (i,j) not in d:
                            d.append((i,j))
                    if (i,j) not in d:
                        point = mas[i][j]
                        d.append((i,j))
                        mas = flow(i,j,point,d,mas)
        for i in mas:
            sum2+=sum(i)
        answer.append(sum2-sum1)
    for i in answer:
        print(i)
    input()

''' Описание flow()
Функция flow() принимает следующие параметры:
i,j - координаты клетки.
point - исходная клетка. (значение)
d - постепенно пополняемый список обработанных клеток острова. (координаты)
mas - Матрица заданного острова.

river=[] - по-умолч. Список рек и течений. 
Соседних клеток <= исходной клетке. Формируется функцией. (координаты)

out={} - по-умолч. Словарь выходов-"сливов" на границах острова.
Координат и значений соседних клеток, являющихся границей острова <= исходной клетке. 
Формируется функцией. (координаты: значения)

path=[] - по-умолч. Локальный список клеток для выхода из рекурсии, пополняемый в течении анализа river.
Формируется функцией. (координаты)

Действия:
1. Проверка клеток в четырех направлениях от исходной (формирование списков d, river, out).
2. Переход на соседние клетки по координатам river посредством рекурсивного вызова функции.
3. Поднятие уровня "воды" в клетках-низинах.
4. Возврат измененного массива.
'''

def flow(i,j,point,d,mas,river=[],out={},path=[]):
    path.append((i,j))
    if (i,j) not in river:
        river.append((i,j))
# 1.Проверка соседних клеток:
    if j+1 == (len(mas[i])-1): # Справа
        out[(i,j+1)] = mas[i][j+1]
        d.append((i,j+1))
    else:
        if mas[i][j+1] <= point and (i,j+1) not in river:
            river.append((i,j+1))
        elif mas[i][j+1] > point and (i,j+1) not in river:
            out[(i,j+1)] = mas[i][j+1]
    if j-1 == 0:               # Слева
        out[(i,j-1)] = mas[i][j-1]
        d.append((i,j-1))
    else:
        if mas[i][j-1] <= point and (i,j-1) not in river:
            river.append((i,j-1))
        elif mas[i][j-1] > point and (i,j-1) not in river:
            out[(i,j-1)] = mas[i][j-1]
    if i+1 == len(mas)-1:      # Снизу
        out[(i+1,j)] = mas[i+1][j]
        d.append((i+1,j))
    else:
        if mas[i+1][j] <= point and (i+1,j) not in river:
            river.append((i+1,j))
        elif mas[i+1][j] > point and (i+1,j) not in river:
            out[(i+1,j)] = mas[i+1][j]
    if i-1 == 0:               # Сверху
        out[(i-1,j)] = mas[i-1][j]
        d.append((i-1,j))
    else:
        if mas[i-1][j] <= point and (i-1,j) not in river:
            river.append((i-1,j))
        elif mas[i-1][j] > point and (i-1,j) not in river:
            out[(i-1,j)] = mas[i-1][j]
# В случае, если клетка имеет непосредственный выход в море:
    if out!={}:
        if point >= min(out.values()):
            river.clear()
            out.clear()
            path.clear()
            return mas
# Рекурсивный вызов:
    if len(river)>1:
        for x,y in river:
            if (x,y) not in path:
                flow(x, y, point, d, mas, river, out)
# Поднятие уровня рек:
    if out!={}:
        for x,y in river:
            if min(out.values())>mas[x][y]:
                mas[x][y] = min(out.values())
                if (x,y) not in d:
                    d.append((x,y))
    river.clear()
    out.clear()
    path.clear()
    return mas

if __name__ == '__main__':
    main()
