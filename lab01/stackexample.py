class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Initial stack:")
stack.display()

print("\nElement popped:", stack.pop())
print("Stack after pop:")
stack.display()

print("\nTop element:", stack.peek())
print("Is stack empty?", stack.is_empty())
print("Size of stack:", stack.size())
