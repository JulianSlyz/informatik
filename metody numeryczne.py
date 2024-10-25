def f(x):
    return 2 * x - 1

a = -1
b = 4
E = 0.000000001

def wb(x):
    if x < 0:
        return -x
    else:
        return x

if f(a) * f(b) <= 0:
    while wb(b - a) > E:
        S = (a + b) / 2
        if f(a) * f(S) <= 0:
            b = S
        else:
            a = S

    print("Przybliżony pierwiastek:", S)
else:
    print("Brak pierwiastków w podanym przedziale")
