while True:
    a = input()
    la = len(a)
    if la > 50:
        print('Подпоследовательность не должна превышать 50 цифр')
    else:
        line = ''
        i = 1
        while i != -1:
            for j in str(i):
                line += j # наращивание последовательности поэлементно
                if len(line) >= la:
                    if line[len(line)-la:len(line)].find(a) != -1: #проверочный срез последовательности
                        print(line.find(a)+1)
                        i = -2
                        break
            i+=1


