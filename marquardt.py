from gradient import gradient, hesse
from norm import norm
from inverse_matrix import inverse_matrix

def marquardt(x0, m, eps, f):
    k = 0
    lam = 100000.0
    x = x0.copy()
    new_grad = True
    while k < m:
        if new_grad:
            grad = gradient(f, x, eps)
            new_grad = False
        if norm(grad) < eps:
            break
        h = hesse(f, x, eps)
        for i in range(len(h)):
            h[i][i] += lam
        h = inverse_matrix(h)
        x1 = x.copy()
        for i in range(len(x1)):
            for j in range(len(h)):
                x1[i] -= h[i][j]*grad[j]
        if f(x1) < f(x):
            lam /= 2
            k += 1
            new_grad = True
            x = x1.copy()
        else:
            lam *= 2
    return x, f(x)

if __name__ == "__main__":
    def f(x):
        return ((x[0]+10*x[1])**2)+5*((x[2]-x[3])**2)+((x[1]-2*x[2])**2)+10*((x[0]-x[3])**4)
    def g(x):
        return 1000*((x[1]-(x[0]**2))**2)+((1-x[0])**2)
    x = [500, 1000, -1000, 1300]
    x1 = [500, -500]
    eps = 0.001
    print(marquardt(x, 500, eps, f))

