class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(2)

    print(q.size())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
