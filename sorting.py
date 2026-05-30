import time

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# Selection Sort
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


# Insertion Sort
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


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

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


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Save Result
def save_result(method, arr, result, execution_time):
    file = open("sorting_results.txt", "a")

    file.write("\n====================================\n")
    file.write("Sorting Method : " + method + "\n")
    file.write("Input Array    : " + str(arr) + "\n")
    file.write("Sorted Array   : " + str(result) + "\n")
    file.write("Execution Time : " + str(execution_time) + " seconds\n")

    file.close()


# Compare All Algorithms
def compare_algorithms(arr):

    print("\n----- Performance Comparison -----")

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    for name, algo in algorithms:

        start = time.perf_counter()
        algo(arr)
        end = time.perf_counter()

        print(f"{name:<15} {(end-start):.8f} sec")


# Main Function
def execution():

    arr = list(map(int, input("\nEnter array elements separated by space: ").split()))

    print("\nOriginal Array:", arr)

    print("\nArray Statistics")
    print("Size    :", len(arr))
    print("Minimum :", min(arr))
    print("Maximum :", max(arr))
    print("Sum     :", sum(arr))
    print("Average :", round(sum(arr) / len(arr), 2))

    print("\nChoose Sorting Method")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Compare All Algorithms")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        compare_algorithms(arr)
        return

    start_time = time.perf_counter()

    if choice == 1:
        result = bubble_sort(arr)
        method = "Bubble Sort"
        time_complexity = "Best: O(n), Average: O(n²), Worst: O(n²)"
        space_complexity = "O(1)"

    elif choice == 2:
        result = selection_sort(arr)
        method = "Selection Sort"
        time_complexity = "Best: O(n²), Average: O(n²), Worst: O(n²)"
        space_complexity = "O(1)"

    elif choice == 3:
        result = insertion_sort(arr)
        method = "Insertion Sort"
        time_complexity = "Best: O(n), Average: O(n²), Worst: O(n²)"
        space_complexity = "O(1)"

    elif choice == 4:
        result = merge_sort(arr)
        method = "Merge Sort"
        time_complexity = "Best: O(n log n), Average: O(n log n), Worst: O(n log n)"
        space_complexity = "O(n)"

    elif choice == 5:
        result = quick_sort(arr)
        method = "Quick Sort"
        time_complexity = "Best: O(n log n), Average: O(n log n), Worst: O(n²)"
        space_complexity = "O(log n)"

    else:
        print("Invalid Choice!")
        return

    end_time = time.perf_counter()

    execution_time = round(end_time - start_time, 8)

    print("\nSorted Array :", result)
    print("Time Complexity  :", time_complexity)
    print("Space Complexity :", space_complexity)
    print("Execution Time   :", execution_time, "seconds")

    save_result(method, arr, result, execution_time)

    print("\nResult saved to sorting_results.txt")


# Program Loop
print("===== SORTING ALGORITHM ANALYZER =====")

while True:

    execution()

    again = input("\nDo you want to sort another array? (y/n): ")

    if again.lower() != "y":
        print("\nThank you for using Sorting Algorithm Analyzer!")
        break
