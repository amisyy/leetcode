import random


def max_heap(heap, heapSize, root):
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if not larger == root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heap(heap, heapSize, larger)


def build_max_heap(heap):
    heapSize = len(heap)
    for i in range((heapSize - 2) // 2, -1, -1):
        max_heap(heap, heapSize, i)


def heapSort(heap):
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        print(heap[i])
        max_heap(heap, i, 0)
    return heap


if __name__ == '__main__':
    a = [30, 50, 9, 10, 11, 57, 77, 62, 78, 94, 80, 84, 1, 2, 3, 4, 5, 6]
    print(a)
    heapSort(a)
    print(a)
    # b = [random.randint(1, 1000) for i in range(1000)]
    # print(b)
    # heapSort(b)
    # print(b)
