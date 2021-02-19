def calculatim(znak,a,b):
    if znak == '+':
        return a + b
    elif znak == '-':
        return a - b
    elif znak == '*':
        return a*b
    elif znak == '/':
        if b==0:
            return 'Деление на ноль!'
        else:
            return a/b
