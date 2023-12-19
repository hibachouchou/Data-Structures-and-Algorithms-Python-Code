#Linked List Algorithms
print("Linked List Algorithms")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Only used in doubly linked list


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        current = self.head

        # Check if the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Element not found")
            return

        prev.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        current = self.head

        # Check if the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        while current and current.data != data:
            current = current.next

        if current is None:
            print("Element not found")
            return

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
