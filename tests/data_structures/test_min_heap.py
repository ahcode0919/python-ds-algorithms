from src.data_structures.min_heap import MinHeap


def test_min_heap_init():
    min_heap = MinHeap()
    assert min_heap.size() == 0


def test_min_heap_insert():
    min_heap = MinHeap()
    min_heap.insert(12)
    min_heap.insert(13)
    min_heap.insert(11)
    min_heap.insert(4)
    min_heap.insert(20)
    min_heap.insert(9)
    min_heap.insert(22)
    min_heap.insert(14)
    assert min_heap.values() == [4, 11, 9, 13, 20, 12, 22, 14]


def test_min_heap_is_empty():
    min_heap = MinHeap()
    assert min_heap.is_empty()

    min_heap.insert(1)
    assert not min_heap.is_empty()


def test_min_heap_size():
    min_heap = MinHeap()
    assert min_heap.size() == 0

    min_heap.insert(12)
    assert min_heap.size() == 1

    min_heap.insert(13)
    assert min_heap.size() == 2

    min_heap.insert(11)
    assert min_heap.size() == 3


def test_min_heap_values():
    min_heap = MinHeap()
    assert min_heap.values() == []

    min_heap.insert(12)
    assert min_heap.values() == [12]

    min_heap.insert(13)
    assert min_heap.values() == [12, 13]

    min_heap.insert(11)
    assert min_heap.values() == [11, 13, 12]
