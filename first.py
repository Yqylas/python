frst = int(input('введите первое число: '))
print(frst)
scnd = input('что будем делать: сложить (+), вычесть (-), умножить(*), делить(/):  ')
print(scnd)
thrd = int(input('введите второе число: '))
while True:
    if scnd == '+':
        print(frst + thrd);
    elif scnd == '-':
        print(frst - thrd);
    elif scnd == '*':
        print(frst * thrd);
    elif scnd == '/' and thrd != 0:
        print(frst / thrd);
    elif scnd == '/' and thrd == 0:
        print('на ноль делить нельзя');
    else:
        print('неизвестная команда')
    break

        