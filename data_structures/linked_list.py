#Linked List 
print("Linked List ")

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
        # Checking if the List is Empty:
        if not self.head:
            # Insertion at the Head if List is Empty
            self.head = new_node
            return
        # If the list is not empty, we start traversing from the head of the list.
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        prev = None
        # This loop traverses the linked list until it reaches the specified index or the end of the list. prev is updated to current in each iteration.
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if count == index:
            # The prev.next pointer is updated to point to the new node.
            prev.next = new_node
            #  The new_node.next pointer is updated to point to the node that was at the specified index.
            new_node.next = current
        else:
            print("Index out of bounds")

    def delete(self, data):
        current = self.head

        # Check if the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        # this loop traverses the linked list until it finds a node with the specified data or reaches the end of the list. prev is updated to current in each iteration.
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Element not found")
            return
        #  If the node with the specified data is found, the prev.next pointer is updated to skip the current node, effectively removing it from the list.
        prev.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        #  This condition checks if the linked list is not empty
        if self.head:
            #
            self.head.prev = new_node
        # The head of the linked list is updated to be the new node. 
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

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        count = 0
        prev = None

        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if count == index:
            prev.next = new_node
            new_node.prev = prev
            new_node.next = current
            if current:
                current.prev = new_node
        else:
            print("Index out of bounds")

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
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage of Singly Linked List
singly_linked_list = SinglyLinkedList()
# Adding elements in the list
singly_linked_list.insert_at_head(3)
singly_linked_list.insert_at_head(2)
singly_linked_list.insert_at_tail(4)
singly_linked_list.insert_at_index(1,8)

print("Singly Linked List:")
singly_linked_list.display()
print("Search for 2:", singly_linked_list.search(2))  # True
print("Search for 5:", singly_linked_list.search(5))  # False

singly_linked_list.delete(2)
print("After deleting 2:")
singly_linked_list.display()

# Example usage of Doubly Linked List
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_at_head(3)
doubly_linked_list.insert_at_head(2)
doubly_linked_list.insert_at_tail(4)
doubly_linked_list.insert_at_index(1,8)

print("Doubly Linked List:")
doubly_linked_list.display()
print("Search for 2:", doubly_linked_list.search(2))  # True
print("Search for 5:", doubly_linked_list.search(5))  # False

doubly_linked_list.delete(2)
print("After deleting 2:")
doubly_linked_list.display()