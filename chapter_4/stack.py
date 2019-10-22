if __name__ == '__main__':
    arr = input().strip().split()
    res = []
    for i in range(len(arr)):
        if arr[i] not in '+-*':
            res.append(int(arr[i]))
        else:
            tmp1 = res.pop()
            tmp2 = res.pop()
            if arr[i] == '+':
                res.append(tmp1 + tmp2)
            elif arr[i] == '-':
                res.append(tmp2 - tmp1)
            else:
                res.append(tmp1 * tmp2)
    print(res[0])
