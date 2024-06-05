class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Initial queue:")
queue.display()

print("\nElement dequeued:", queue.dequeue())
print("Queue after dequeue:")
queue.display()

print("\nFront element:", queue.peek())
print("Is queue empty?", queue.is_empty())
print("Size of queue:", queue.size())

