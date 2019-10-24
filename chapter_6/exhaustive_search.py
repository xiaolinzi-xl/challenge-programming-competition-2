def reboot(arr, index, count, q):
    if index >= len(arr):
        return False
    if count > q:
        return False
    if count + arr[index] == q:
        return True
    elif count + arr[index] > q:
        return reboot(arr, index + 1, count, q)
    return reboot(arr, index + 1, count + arr[index], q) or reboot(arr, index + 1, count, q)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    q_arr = list(map(int, input().split()))
    min_ele = arr[0]
    arr_sum = arr[0]
    for i in range(1, len(arr)):
        min_ele = min(min_ele, arr[i])
        arr_sum += arr[i]
    for ele in q_arr:
        if ele < min_ele or ele > arr_sum:
            print('no')
        else:
            if reboot(arr, 0, 0, ele):
                print('yes')
            else:
                print('no')
