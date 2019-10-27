def count_sort(arr, max_element=10000):
    c = [0] * (max_element + 1)

    for ele in arr:
        c[ele] += 1
    index = 0
    for i in range(len(c)):
        while c[i] != 0:
            arr[index] = i
            index += 1
            c[i] -= 1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    count_sort(arr)

    arr = map(str, arr)
    print(' '.join(arr))
