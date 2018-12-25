def norm(x):
    norm = 0.0
    for i in range(len(x)):
        norm += (x[i]**2)
    return norm**0.5

if __name__ == "__main__":
    x = [3, 4]
    print(norm(x))