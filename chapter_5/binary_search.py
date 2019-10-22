def search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False


if __name__ == '__main__':
    n = int(input())
    arr_1 = list(map(int, input().split()))
    q = int(input())
    arr_2 = list(map(int, input().split()))
    ans = 0
    for element in arr_2:
        if search(arr_1, element):
            ans += 1
    print(ans)
