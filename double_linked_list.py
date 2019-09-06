class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
    # Add Node at the end
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None
    # Add Node at the beginning
    def preappend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Add Node at specific position
    def append_after(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
            elif current_node.data == key:
                new_node = Node(data)
                next = current_node.next
                current_node.next = new_node
                new_node.next = next
                next.prev = new_node
            current_node = current_node.next
    #print the list
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    # length of the list
    def length(self):
        current_node = self.head
        total = 1
        while current_node:
            current_node = current_node.next
            total += 1
        return total

list = DoubleLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(5)
list.preappend(0)
list.append_after(3,4)
list.show()
n = list.length()
print(f"Length of the List is: {n}")
