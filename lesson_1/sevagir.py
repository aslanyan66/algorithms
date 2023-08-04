from random import randint
def search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        current = arr[mid]

        if current == target:
            return mid

        if target > current:
            low = mid + 1

        if target < current:
            high = mid - 1

    return -1

numbers = sorted([randint(0, 50000000) for _ in range(256)])

search(numbers, numbers[0])