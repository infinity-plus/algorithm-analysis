def bubble_sort(arr: list[int]) -> tuple[list[int], int]:
    n = len(arr)
    inversions = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                inversions += 1
    return arr, inversions


def selection_sort(arr: list[int]) -> tuple[list[int], int]:
    inversions = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        inversions += 1
    return arr, inversions


def insertion_sort(arr: list[int]) -> tuple[list[int], int]:
    inversions = 0
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            # Swap:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1
            inversions += 1
        arr[j + 1] = key

    return arr, inversions


def merge_sort(arr: list[int], inv: int = 0) -> tuple[list[int], int]:
    inversions = 0 + inv
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        left, inv1 = merge_sort(left, inversions)
        right, inv2 = merge_sort(right, inversions)
        inversions += inv1 + inv2

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                arr[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            inversions += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            inversions += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            inversions += 1
    return arr, inversions


def quick_sort(arr: list[int], inv: int = 0) -> tuple[list[int], int]:
    elements = len(arr)
    inversions = 0 + inv
    # Base case
    if elements < 2:
        return arr, inversions
    cur_pos = 0  # Position of the partitioning element
    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            cur_pos += 1
            arr[i], arr[cur_pos] = arr[cur_pos], arr[i]
            inversions += 1
    # Brings pivot to it's appropriate position
    arr[0], arr[cur_pos] = arr[cur_pos], arr[0]
    inversions += 1

    left, inv1 = quick_sort(arr[:cur_pos], inversions)
    right, inv2 = quick_sort(
        arr[cur_pos + 1 : elements], inversions
    )  # sorts the elements to the right of pivot
    inversions += inv1 + inv2
    arr = left + [arr[cur_pos]] + right  # Merging everything together

    return arr, inversions
