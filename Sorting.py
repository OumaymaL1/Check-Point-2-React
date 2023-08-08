def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current_element

# Example usage
input_array = [5, 2, 9, 1, 5, 6]
insertion_sort(input_array)
print("Sorted array:", input_array)
