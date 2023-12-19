#Queue Algorithms
print("Queue Algorithms")

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. Cannot peek.")

    def contains(self, item):
        return item in self.items

    def removal(self, item):
        if self.contains(item):
            self.items.remove(item)
        else:
            print(f"Item {item} not found in the queue.")

    def size(self):
        return len(self.items)


# Example usage of the queue