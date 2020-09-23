def decimal_translator(number, base):
    base = int(base)
    a = 0
    for i in range(len(number)):
        if int(number[i - 1]) >= base:
            a = int(number[i - 1]) // base
            a += a * (10 ** i)
        elif int(number[i - 1]) <= base:
            a = (int(number[i - 1]) * 10 + int(number[i])) // base
            a += a * (10 ** i)
decimal_translator(number, base)