class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def insert_after(self, node, data):
        new_node = Node(data)
        if node is None:
            return
        new_node.prev = node
        new_node.next = node.next
        node.next = new_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def insert_before(self, node, data):
        new_node = Node(data)
        if node is None:
            return
        new_node.next = node
        new_node.prev = node.prev
        node.prev = new_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def delete_at_end(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


fruits = DoublyLinkedList()
fruits.append('banana')
fruits.append('manggo')
fruits.insert_after(fruits.head.next, 'apple')
fruits.append('grapes')
fruits.append('orange')
fruits.insert_before(fruits.tail.prev ,'durian')
fruits.delete_at_end()

fruits.print_list()
