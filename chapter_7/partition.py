def partition(arr, p, r):
    x = arr[r]
    index = p - 1  # arr[p,index] <= x,arr[index+1,i)>x
    for i in range(p, r):
        if arr[i] <= x:
            arr[i], arr[index + 1] = arr[index + 1], arr[i]
            index += 1
    arr[index + 1], arr[r] = arr[r], arr[index + 1]
    return index + 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    index = partition(arr, 0, n - 1)
    for i in range(n):
        if i != 0:
            print(' ', end='')
        if i == index:
            print('[', end='')
        print(arr[i], end='')
        if i == index:
            print(']', end='')
    print()
