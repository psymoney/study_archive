from SinglyLinkedList import *


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
