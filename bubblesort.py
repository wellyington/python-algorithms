def bubblesort2(array,size):
    for x in range(0, size - 1):
        for i in range(0, size - 1):
            if array[i] > array[i + 1]:
                _swap = array[i]
                array[i] = array[i + 1]
                array[i + 1] = _swap
    print(x, array)