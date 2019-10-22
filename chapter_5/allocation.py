def judge(arr, p, k):
    count = 0
    weight_sum = 0
    for ele in arr:
        if ele > p:
            return False
        if weight_sum + ele < p:
            weight_sum += ele
        elif weight_sum + ele == p:
            weight_sum = 0
            count += 1
        else:
            weight_sum = ele
            count += 1
        if count > k:
            return False
    if weight_sum != 0:
        count += 1
    return count <= k


if __name__ == '__main__':
    n, k = map(int, input().split())
    weight = []
    l, r = 0, 0
    for _ in range(n):
        tmp = int(input())
        weight.append(tmp)
        r += tmp
        l = max(l, tmp)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if judge(weight, mid, k):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
