

def swap(arry, i, j):
    tmp = arry[i]
    arry[i] = arry[j]
    arry[j] = tmp


def adjust_heap(arry, i, length):
    max_index = i
    if 2*i+1 < length and arry[2*i+1] > arry[max_index]:
        max_index = 2*i+1

    if 2*i+2 < length and arry[2*i+2] > arry[max_index]:
        max_index = 2*i+2

    if max_index != i:
        swap(arry, max_index, i)
        adjust_heap(arry, max_index, length)


def build_max_heap(arry, length):
    i = length // 2 - 1
    while i >= 0:
        adjust_heap(arry, i, length)
        i -= 1


def heap_sort(arry):
    length = len(arry)
    if length < 1:
        return arry
    build_max_heap(arry, length)
    while length > 0:
        swap(arry, 0, length-1)
        length -= 1
        adjust_heap(arry, 0, length)
    return arry


if __name__ == '__main__':
    import random
    arry = [random.randint(0, 100) for i in range(20)]
    print(arry)
    print(heap_sort(arry))



