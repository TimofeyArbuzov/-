def perevod(n):
    f = 0
    a, n = n.split('(')
    for i in range(len(a)):
        f = (int(a[i]) * (int(n) ** (len(a) - i)))  + f
    return f