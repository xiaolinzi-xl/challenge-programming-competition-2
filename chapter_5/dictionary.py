if __name__ == '__main__':
    record = set()
    n = int(input())
    for _ in range(n):
        order, string = input().split()
        if order == 'insert':
            record.add(string)
        else:
            assert order == 'find', '输入错误'
            if string in record:
                print('yes')
            else:
                print('no')
