class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, data):
        self.next = Node(data)

    def get_next(self):
        return self.next

    def append(self, data):
        while self.get_next() is not None:
            self.set_next(self.get_next())
        self.set_next(data)

    def retrieve(self):
        while self.next is not None:
            self = self.next
            print(f'{self.get_data}', end=' > ')


if __name__ == '__main__':
    head = Node(None)
    head.set_next(1)
    head.retrieve()

