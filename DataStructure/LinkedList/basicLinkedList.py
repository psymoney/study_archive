class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None, next=None):
        if data is not None:
            self.next = Node(data)
        else:
            self.next = next
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


def get_linked_list_with_three_nodes():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    return linked_list


def get_linked_list_with_five_nodes():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    return linked_list


def test_push_method():
    print('LinkList push(self, data) method test')

    print('\tcase #1: push when the given LinkedList is empty')
    linked_list = LinkedList()
    linked_list.push(2)
    if linked_list.next.data != 2:
        print('\tㄴresult: fail')
    elif linked_list.length != 1:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')

    print('\tcase #2: push when the given LinkedList is not empty')
    linked_list.push(1)
    if linked_list.next.data != 1:
        print('\tㄴresult: fail')
    elif linked_list.length != 2:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')
    print('')


def test_append_method():
    print('LinkList append(self, data) method test')

    print('\tcase #1: append when the given LinkedList is empty')
    linked_list = LinkedList()
    linked_list.append(1)
    if linked_list.next.data != 1:
        print('\tㄴresult: fail')
    elif linked_list.length != 1:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')

    print('\tcase #2: append when the given LinkedList is not empty')
    linked_list.append(2)
    if linked_list.next.next.data != 2:
        print('\tㄴresult: fail')
    elif linked_list.length != 2:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')
    print('')


def test_retrieve_method():
    print('LinkedList retrieve() method test')
    linked_list = get_linked_list_with_five_nodes()
    print('result: ')
    linked_list.retrieve()
    print('')


def test_insert_method(debug=False):
    print('LinkedList insert(self, position, data) method test')

    print('\tcase #1: insert data into the first node')
    linked_list = get_linked_list_with_five_nodes()
    linked_list.insert(0, 0)
    if linked_list.next.data != 0:
        print('\tㄴresult: fail')
    elif linked_list.next.next.data != 1:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.data != 2:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.data != 3:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.data != 4:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.next.data != 5:
        print('\tㄴresult: fail')
    elif linked_list.length != 6:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')
    if debug is True:
        print('debug >> ')
        linked_list.retrieve()

    print('\tcase #2: insert data into the last node')
    linked_list = get_linked_list_with_five_nodes()
    linked_list.insert(5, 6)

    if linked_list.next.data != 1:
        print('\tㄴresult: fail')
    elif linked_list.next.next.data != 2:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.data != 3:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.data != 4:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.data != 5:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.next.data != 6:
        print('\tㄴresult: fail')
    elif linked_list.length != 6:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')
    if debug is True:
        print('debug >> ')
        linked_list.retrieve()

    print('\tcase #3: insert data into the third node')
    linked_list = get_linked_list_with_five_nodes()
    linked_list.insert(3, 0)
    if linked_list.next.data != 1:
        print('\tㄴresult: fail')
    elif linked_list.next.next.data != 2:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.data != 0:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.data != 3:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.data != 4:
        print('\tㄴresult: fail')
    elif linked_list.next.next.next.next.next.next.data != 5:
        print('\tㄴresult: fail')
    elif linked_list.length != 6:
        print('\tㄴresult: fail')
    else:
        print('\tㄴresult: success')
    if debug is True:
        print('debug >> ')
        linked_list.retrieve()
    print('')


def test_pop_method(debug=False):
    print('LinkedList pop() method test')

    linked_list = get_linked_list_with_three_nodes()
    linked_list.pop()
    if linked_list.next.data != 2:
        print('ㄴresult: fail')
    elif linked_list.next.next.data != 3:
        print('ㄴresult: fail')
    elif linked_list.length != 2:
        print('ㄴresult: fail')
    else:
        print('ㄴresult: success')

    if debug is True:
        print('debug>> ')
        linked_list.retrieve()
    print('')


def test_remove_method(debug=False):
    print('LinkedList remove() method test')

    linked_list = get_linked_list_with_three_nodes()
    linked_list.remove()

    if linked_list.next.data != 1:
        print('ㄴresult: fail')
    if linked_list.next.next.data != 2:
        print('ㄴresult: fail')
    if linked_list.next.next.next is not None:
        print('ㄴresult: fail')
    elif linked_list.length != 2:
        print('ㄴresult: fail')
    else:
        print('ㄴresult: success')

    if debug is True:
        print('debug>>')
        linked_list.retrieve()
    print('')


if __name__ == '__main__':
    test_push_method()
    test_append_method()
    test_retrieve_method()
    test_insert_method()
    test_pop_method()
    test_remove_method()
