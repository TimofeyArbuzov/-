def decimal_translator_2(number, base):
    number = str(number)[::-1]
    count = 0
    for i in range(len(number)):
        a = number[i]
        if not a.isdigit():
            a = ord(a) - 55
        else:
            a = int(a)
        if a >= base:
            return 'None'
        count += a * (base ** i)
    return count
