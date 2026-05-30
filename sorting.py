import time


def selection_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# User Input
choice = 0
def execution():
    arr = list(map(int, input("Enter array elements separated by space: ").split()))

    print("\nOriginal Array:", arr)

    print("\nChoose Sorting Method")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")


    choice = int(input("Enter your choice: "))

    start_time = time.perf_counter()

    if choice == 1:
        result = bubble_sort(arr)
        complexity = "Best: O(n), Average: O(n²), Worst: O(n²)"

    elif choice == 2:
        result = selection_sort(arr)
        complexity = "Best: O(n²), Average: O(n²), Worst: O(n²)"

    elif choice == 3:
        result = insertion_sort(arr)
        complexity = "Best: O(n), Average: O(n²), Worst: O(n²)"

    elif choice == 4:
        result = merge_sort(arr)
        complexity = "Best: O(n log n), Average: O(n log n), Worst: O(n log n)"

    elif choice == 5:
        result = quick_sort(arr)
        complexity = "Best: O(n log n), Average: O(n log n), Worst: O(n²)"

    else:
        print("Invalid Input")
        return

    end_time = time.perf_counter()

    print("\nSorted Array:", result)
    print("Time Complexity:", complexity)
    print(f"Execution Time: {(end_time - start_time):.8f} seconds")

execution()


sort_more = input("Do You wanna Sort more?(y/n): ")
if sort_more.lower() == "y":
    while True:
        execution()

