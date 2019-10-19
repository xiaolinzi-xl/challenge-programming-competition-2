def print_arr(arr):
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i], end=' ')
        else:
            print(arr[i], end='')
    print()


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print_arr(arr)
    for i in range(1, len(arr)):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v
        print_arr(arr)
