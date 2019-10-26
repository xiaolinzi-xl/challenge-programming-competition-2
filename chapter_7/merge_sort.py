global count


def merge(arr, l, mid, r):
    arr_l = list(arr[l:mid + 1])
    arr_r = list(arr[mid + 1:r + 1])
    l_index = 0
    r_index = 0
    arr_l.append(2 << 64)
    arr_r.append(2 << 64)
    global count
    for i in range(l, r + 1):
        if arr_l[l_index] <= arr_r[r_index]:
            arr[i] = arr_l[l_index]
            l_index += 1
        else:
            arr[i] = arr_r[r_index]
            r_index += 1
        count += 1


def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


if __name__ == '__main__':
    count = 0

    n = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, len(arr) - 1)
    for i in range(n):
        if i != n - 1:
            print(arr[i], end=' ')
        else:
            print(arr[i])
    print(count)
