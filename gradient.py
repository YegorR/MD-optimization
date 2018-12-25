import math


def gradient(f, x, eps):
    n = len(x)
    grad = [0.0 for _ in range(n)]
    for i in range(n):
        dx = 0.01
        x0 = x.copy()
        x0[i] += dx
        y1 = (f(x0) - f(x)) / dx
        dx /= 10
        x0 = x.copy()
        x0[i] += dx
        y2 = (f(x0) - f(x)) / dx
        dif = math.fabs(y2-y1)
        while dif >= eps:
            y1 = y2
            dx /= 10
            x0 = x.copy()
            x0[i] += dx
            y2 = (f(x0) - f(x)) / dx
            if math.fabs(y2-y1) > dif:
                break
            dif = math.fabs(y2-y1)
        grad[i] = y2
    return grad

def hesse_m(f, x, eps, a, b):
    if a == b:
        dx = 0.01
        x0 = x.copy()
        x1 = x.copy()
        x0[a] += dx
        x1[a] -= dx
        y1 = (f(x0)-2*f(x)+f(x1))/(dx**2)
        dx /= 10
        x0 = x.copy()
        x1 = x.copy()
        x0[a] += dx
        x1[a] -= dx
        y2 = (f(x0)-2*f(x)+f(x1))/(dx**2)
        dif = math.fabs(y2 - y1)
        while dif >= eps:
            y1 = y2
            dx /= 10
            x0 = x.copy()
            x1 = x.copy()
            x0[a] += dx
            x1[a] -= dx
            y2 = (f(x0) - 2 * f(x) + f(x1)) / (dx ** 2)
            if math.fabs(y2 - y1) > dif:
                break
            dif = math.fabs(y2 - y1)
        return y2
    else:
        def get_args(dx):
            x0 = x.copy()
            x1 = x.copy()
            x2 = x.copy()
            x3 = x.copy()
            x0[a] += dx
            x0[b] += dx
            x1[a] += dx
            x1[b] -= dx
            x2[a] -= dx
            x2[b] += dx
            x3[a] -= dx
            x3[b] -= dx
            return x0, x1, x2, x3

        dx = 0.01
        x0, x1, x2, x3 = get_args(dx)
        y1 = (f(x0)-f(x1)-f(x2)+f(x3))/(4*(dx**2))
        dx /= 10
        x0, x1, x2, x3 = get_args(dx)
        y2 = (f(x0)-f(x1)-f(x2)+f(x3))/(4*(dx**2))
        dif = math.fabs(y2 - y1)
        while dif >= eps:
            y1 = y2
            dx /= 10
            x0, x1, x2, x3 = get_args(dx)
            y2 = (f(x0)-f(x1)-f(x2)+f(x3))/(4*(dx**2))
            if math.fabs(y2 - y1) > dif:
                break
            dif = math.fabs(y2 - y1)
        return y2


def hesse(f, x, eps):
    n = len(x)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = hesse_m(f, x, eps, i, j)
            matrix[j][i] = matrix[i][j]
    return matrix

if __name__ == "__main__":
    x = [1000, 1000, 1000, 1000]
    f = lambda x: ((x[0]+10*x[1])**2)+5*((x[2]-x[3])**2)+((x[1]-2*x[2])**4)+10*((x[0]-x[3])**4)
    eps = 0.001
    #print(gradient(f, x, eps))
    m = hesse(f, x, eps)
    for i in range(len(x)):
        print(m[i])
