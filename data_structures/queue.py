#Queue 
print("Queue")

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
    
    def display(self):
        if not self.is_empty():
            print("Front of the Queue:", end=" ")
            for item in self.items:
                print(item, end=" ")
            print(": Rear of the Queue")
        else:
            print("Queue is empty.")


# Example usage of the queue
queue = Queue()

# Enqueuing elements into the queue
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)

print("Queue:")
queue.display()
print("Is empty?", queue.is_empty())  # False
print("Size:", queue.size())          # 3
print("Peek:", queue.peek())          # 2

# Dequeuing elements from the queue
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)    # 2
print("Size after dequeue:", queue.size()) # 2
queue.display()

# Checking if the queue contains an element
print("Contains 4?", queue.contains(4))  # True
print("Contains 8?", queue.contains(8))  # False

# Removing a specific element from the queue
queue.removal(4)
print("Size after removal:", queue.size()) # 1
queue.display()

# Checking if the queue is empty
print("Is empty?", queue.is_empty())  # False