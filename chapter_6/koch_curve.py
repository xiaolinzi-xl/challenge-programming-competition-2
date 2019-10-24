import math


def koch(count, p1, p2):
    if count == 0:
        return
    s = [0, 0]
    t = [0, 0]
    u = [0, 0]
    s[0] = (2 * p1[0] + p2[0]) / 3
    s[1] = (2 * p1[1] + p2[1]) / 3
    t[0] = (2 * p2[0] + p1[0]) / 3
    t[1] = (2 * p2[1] + p1[1]) / 3
    u[0] = (t[0] - s[0]) * math.cos(math.pi / 3) - (t[1] - s[1]) * math.sin(math.pi / 3) + s[0]
    u[1] = (t[0] - s[0]) * math.sin(math.pi / 3) + (t[1] - s[1]) * math.cos(math.pi / 3) + s[1]

    koch(count - 1, p1, s)
    print(s[0], s[1])

    koch(count - 1, s, u)
    print(u[0], u[1])

    koch(count - 1, u, t)
    print(t[0], t[1])

    koch(count - 1, t, p2)


if __name__ == '__main__':
    n = int(input())
    p1 = [0.0, 0.0]
    p2 = [100.0, 0.0]
    print(p1[0], p1[1])
    koch(n, p1, p2)
    print(p2[0], p2[1])
