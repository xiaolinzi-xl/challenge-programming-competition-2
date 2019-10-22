from queue import Queue


class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = Queue()
    for _ in range(n):
        name, time = input().split()
        arr.put(Task(name, int(time)))
    all_time = 0
    while not arr.empty():
        task = arr.get()
        if task.time > q:
            arr.put(Task(task.name, task.time - q))
            all_time += q
        else:
            all_time += task.time
            print(task.name, all_time)
