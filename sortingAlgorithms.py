# Heap Sort
def heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapSort(arr, l):
    i = l
    while i >= 0:
        heap(arr, l, i)
        i -= 1

    j = l - 1
    while j > 0:
        arr[j], arr[0] = arr[0], arr[j]
        heap(arr, j, 0)
        j -= 1


def main():
    arr = []
    l = int(input("Enter the length of the array: "))
    for x in range(l):
        x = int(input("Enter the array elements: "))
        arr.append(x)
    heapSort(arr, l)

    print(arr)


if __name__ == "__main__":
    main()


# Quick Sort
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def main():
    arr = []
    l = int(input("Enter the length of the array: "))
    for x in range(l):
        x = int(input("Enter the array elements: "))
        arr.append(x)

    quickSort(arr, 0, l-1)

    print(arr)


if __name__ == "__main__":
    main()
    
# Counting Sort
def countSort(arr, m):
    c = []
    output = [0 for i in range(1, m+1)]
    i = 0
    for i in range(m+1):
        c.append(0)
    for a in arr:
        c[a] += 1
    for i in range(1, m+1):
        c[i] += c[i-1]
    for a in arr:
        x = c[a]
        output[x] = a
        c[a] -= 1

    return output


def main():
    arr = []
    l = int(input("Enter the length of the array: "))
    for x in range(l):
        x = int(input("Enter the array elements: "))
        arr.append(x)
    m = max(arr)
    print(countSort(arr, m))


if __name__ == "__main__":
    main()
