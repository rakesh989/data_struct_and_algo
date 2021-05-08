# Binary_search( only work is sorted data)
def binary_search(arr, number, low, high):
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if number == arr[mid]:
            return mid
        elif number < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(arr))
num = int(input("enter the no to find"))
x = binary_search(arr, num, 0, len(arr))
if x == -1:
    print("no does not exist")
else:
    print("found at position", x)