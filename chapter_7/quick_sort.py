class Card:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __le__(self, other):
        return self.number <= other.number

    def __str__(self):
        return f'{self.name} {self.number}'


def partition(arr, p, r):
    x = arr[r]
    index = p - 1  # arr[p,index] <= x,arr[index+1,i)>x
    for i in range(p, r):
        if arr[i] <= x:
            arr[i], arr[index + 1] = arr[index + 1], arr[i]
            index += 1
    arr[index + 1], arr[r] = arr[r], arr[index + 1]
    return index + 1


def quick_sort(arr, l, r):
    if l >= r:
        return
    q = partition(arr, l, r)
    quick_sort(arr, l, q - 1)
    quick_sort(arr, q + 1, r)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        name, number = input().split()
        arr.append(Card(name, int(number)))
    sort_before_record = {}
    for ele in arr:
        if ele.number in sort_before_record:
            sort_before_record[ele.number].append(ele.name)
        else:
            sort_before_record[ele.number] = [ele.name]

    quick_sort(arr, 0, n - 1)

    sort_after_record = {}
    for ele in arr:
        if ele.number in sort_after_record:
            sort_after_record[ele.number].append(ele.name)
        else:
            sort_after_record[ele.number] = [ele.name]
    flag = True

    for key in sort_before_record:
        if sort_before_record[key] != sort_after_record[key]:
            flag = False
            break

    if flag:
        print('Stable')
    else:
        print('Not stable')
    for ele in arr:
        print(ele)
