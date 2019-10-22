if __name__ == '__main__':
    n = int(input())
    arr_1 = set(map(int, input().split()))
    q = int(input())
    arr_2 = set(map(int, input().split()))
    arr = arr_1 & arr_2
    print(len(arr))
