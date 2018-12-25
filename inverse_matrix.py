import copy


def gauss_direct(a, b, n):
    for i in range(n):
        for j in range(i+1, n):
            m = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= a[i][k] * m
            b[j] -= b[i] * m


def gauss_reverse(a, b, n):
    x = [None for _ in range(n)]
    for i in range(n-1, -1, -1):
        s = 0.0
        for j in range(i+1, n):
            s += a[i][j]*x[j]
        x[i] = (b[i] - s) / a[i][i]
    return x


def gauss(a, b, n):
    bn = copy.copy(b)
    an = copy.deepcopy(a)
    gauss_direct(an, bn, n)
    return gauss_reverse(an, bn, n)


def inverse_matrix(a):
    n = len(a)
    rev = [[0.0] * n for _ in range(n)]
    for i in range(n):
        b = [0.0 for _ in range(n)]
        b[i] = 1.0
        x = gauss(a, b, n)
        for j in range(n):
            rev[j][i] = x[j]
    return rev


if __name__=="__main__":
    a = [[1.9963408703915773, -4000], [-4000, 2000]]
    b = inverse_matrix(a)
    for i in range(len(b)):
        print(b[i])