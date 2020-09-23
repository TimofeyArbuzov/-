def decimal_translator(num, base):
    newnum = ''
    if 2 <= base <= 9:
        while num > 0:
            newnum = str(num % base) + newnum
            num //= base
    return(newnum)
