n = int(input())
a = list(map(int, input().split(' ')))

def search_loop(a, n, s, x, y):
    ax = a.copy()
    ay = a.copy()
    ax[x - 1] = s
    ay[y - 1] = s
    h = []
    g = []
    i = 0
    for k in range(n):
        if ax[i] not in h:
            h.append(ax[i])
            i = ax[i] - 1
    for k in range(n):
        if ay[i] not in g:
            g.append(ay[i])
            i = ay[i] - 1

    if len(h) == n:
        print(x, s)
    elif len(g) == n and len(h) != n:
        print(y, s)
    else:
        return print(-1, -1)
    return 0

def test_arr(a, n):
    count, self, d = 0, 0, 0
    for i in range(n):
        if a[i] == i + 1:
            self += 1
            d = i + 1

        for j in range(i + 1, n):
            if a[i] == a[j]:
                count += 1
                x = i + 1
                y = j + 1
                b = a[i]

    if d: b = d
    if count == 1 and self <= 1:
        s = abs((1 + n) * n / 2 + b - sum(a))
        s = int(s)
    else:
        return print(-1, -1)
    return search_loop(a, n, s, x, y)
test_arr(a, n)
