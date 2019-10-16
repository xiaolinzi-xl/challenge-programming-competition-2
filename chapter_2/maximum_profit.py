if __name__ == '__main__':
    n = int(input())
    assert n >= 2, '输入至少包含两个数'
    a = int(input())
    b = int(input())
    res = b - a
    min_value = min(a, b)
    for _ in range(n - 2):
        tmp = int(input())
        if tmp - min_value > res:
            res = tmp - min_value
        if tmp < min_value:
            min_value = tmp
    print(res)
