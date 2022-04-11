class Node:
    def __init__(self, data=None, node=None):
        self.data = data
        self.next = node


class LinkedList:
    def __init__(self, data=None, node=None):
        if data is not None:
            self.next = Node(data)
        else:
            self.next = node
        self.length = 0

    def push(self, data):
        node = Node(data, self.next)
        self.next = node
        self.length += 1

    def append(self, data):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(data)
        self.length += 1

    def retrieve(self):
        current = self.next
        while current.next is not None:
            print(f'{current.data}', end=' > ')
            current = current.next
        print(current.data)

    def insert(self, position, data):
        if position > self.length or position < 0:
            return None

        if position == self.length:
            self.append(data)
        elif position == 0:
            self.push(data)
        else:
            current = self
            count = 0
            while count < position-1:
                count += 1
                current = current.next
            node = Node(data, current.next)
            current.next = node
            self.length += 1

    def pop(self):
        temp_node = self.next.next
        self.next = temp_node
        self.length -= 1

    def remove(self):
        previous_node = self
        current_node = self
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        self.length -= 1

    def delete_by_position(self, position: int):
        if position < 0 or position > self.length:
            return None
        if position == 0:
            self.pop()
        elif position == self.length:
            self.remove()
        else:
            current_node = self
            previous_node = self
            count = 0
            if count < self.length:
                count += 1
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = current_node.next
            self.length -= 1
