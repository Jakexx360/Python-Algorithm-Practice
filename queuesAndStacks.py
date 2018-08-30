# FIFO
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# LIFO
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Queue implemented with Stacks
class QueueStack:
    def __init__(self):
        self.incoming = Stack()
        self.outgoing = Stack()

    def enqueue(self, item):
        while self.outgoing.size() > 0:
            self.incoming.push(self.outgoing.pop())
        self.incoming.push(item)

    def dequeue(self):
        while self.incoming.size() > 0:
            self.outgoing.push(self.incoming.pop())
        self.outgoing.pop()
