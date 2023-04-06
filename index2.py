class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublelinkedlist:

    def __init__(self):
        self.head = None

    def prepend(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def insert_after(self, key, new_data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(new_data)
            elif curr.data == key:
                new_node = Node(new_data)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            curr = curr.next

    def insert_before(self, key, data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                curr.prev = new_node
                new_node.next = curr
            curr = curr.next


    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.start_node.prev is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



list1 = doublelinkedlist()
list1.append('banana')
list1.append('mango')
list1.append('grapes')
list1.append('orange')
list1.insert_after('mango', 'apple')
list1.insert_before('grapes', 'durian')
list1.delete_at_end()
list1.printlist()
