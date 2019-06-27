### Explanation for Sorting Algorithms

#### Heap Sort
Heapsort is a comparison-based algorithm that uses a binary heap data structure to sort elements. It divides its input into a sorted and an unsorted region, and it iteratively shrinks the unsorted region by extracting the largest element and moving that to the sorted region.
In this algorithm we first build a heap using given elements.We create a **Max Heap** to sort the elements in ascending order .Once the heap is created we swap the root node with the last node and delete the last node from the heap.

#### Counting Sort
Counting sort is a sorting techmique based on key values in specific range.It works by counting the number of objects having distinct key values,then doing some arithmatic calculation to calculate the position of each object in the output sequence.The count of each number is initialised in an array and each value is updated by adding the previous value.We then take an array with length equal to number of inputs
and initialise each number at the corresponding position and decrease the count.The array will be sorted.

#### Quick Sort
This sorting algorithm uses the idea of divide and conquer.It finds the element called pivot which divides the array into two halves such that the elements on the right half of pivot are greater than it and elements on left are lesser.This is done repeatedly till the array is sorted.The position of pivot is changed acoordingly and the left and right part are sorted seperately. 
