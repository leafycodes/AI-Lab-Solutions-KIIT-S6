import random
import yoursearch
import yoursort

n = int(input("Enter number of elements: "))
list = random.sample(range(1, 100), n)
print(f"Original List: {list}")

yoursort.bubble_sort(list)
print(f"Sorted List (Bubble Sort): {list}")

yoursort.insertion_sort(list)
print(f"Sorted List (Insertion Sort): {list}")

yoursort.selection_sort(list)
print(f"Sorted List (Selection Sort): {list}")

key = int(input("Enter element to search: "))

index = yoursearch.linear_search(list, key)
print(f"Linear Search: {'Element found at index ' + str(index) if index != -1 else 'Element not found'}")

index = yoursearch.binary_search(list, key)
print(f"Binary Search: {'Element found at index ' + str(index) if index != -1 else 'Element not found'}")
