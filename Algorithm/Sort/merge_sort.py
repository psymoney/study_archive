

def merge(a, b):
    merged_array = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_array.append(a[i])
            i += 1
        elif b[j] < a[i]:
            merged_array.append(b[j])
            j += 1

    if i != len(a):
        merged_array += a[i:]
    if j != len(b):
        merged_array += b[j:]

    return merged_array


def merge_sort(array, l, r):
    if l >= r:
        return [array[l]]

    mid = (l + r) // 2

    a = merge_sort(array, l, mid)
    b = merge_sort(array, mid + 1, r)

    return merge(a, b)


def test_cases():
    array = [4, 3, 7, 2, 1]
    m_a = merge_sort(array, 0, len(array) - 1)
    print(m_a)

    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    m_a = merge_sort(array, 0, len(array) - 1)
    print(m_a)

    array = [1]
    m_a = merge_sort(array, 0, len(array) - 1)
    print(m_a)


if __name__ == '__main__':
    test_cases()