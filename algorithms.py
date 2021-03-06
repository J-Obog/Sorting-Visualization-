#BUBBLE 
def bubbleSort(arr, gInterface, sInterface):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0,i,1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            gInterface.rerender(arr, [j,j+1])
            sInterface.updateSwaps()

#INSERTION
def insertionSort(arr, interface):
    for i in range(1, len(arr), 1):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
            interface.rerender(arr, [j-1,j])

#SELECTION 
def selectionSort(arr, interface):
    for i in range(0, len(arr), 1):
        min = i
        for j in range(i, len(arr), 1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        interface.rerender(arr, [i,min])
