#Stack 
print("Stack")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")

    def search(self, item):
        return item in self.items

    def size(self):
        return len(self.items)
    
    def display(self):
        if not self.is_empty():
            print("Top of the Stack")
            for item in reversed(self.items):
                print("|", item, "|")
            print("Bottom of the Stack")
        else:
            print("Stack is empty.")

# Example usage of the stack
stack = Stack()

# Pushing elements onto the stack
stack.push(3)
stack.push(5)
stack.push(7)

print("Stack:")
stack.display()
print("Is empty?", stack.is_empty())  # False
print("Size:", stack.size())          # 3
print("Peek:", stack.peek())          # 7

# Popping elements from the stack
popped_item = stack.pop()
print("Popped item:", popped_item)    # 7
print("Size after pop:", stack.size()) # 2
stack.display()

# Searching for an element in the stack
print("Search for 5:", stack.search(5))  # True
print("Search for 10:", stack.search(10)) # False