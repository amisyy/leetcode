def quickSort(nums):
    if len(nums) <= 1:
        return nums
    less = []
    more = []
    base = nums.pop()
    for i in nums:
        if i < base:
            less.append(i)
        else:
            more.append(i)
    return quickSort(less) + [base] + quickSort(more)


def partition(arr, low, high):
    i = low - 1
    base = arr[high]
    for j in range(low, high):
        if arr[j] <= base:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        base_index = partition(arr, low, high)
        quick_sort(arr, low, base_index - 1)
        quick_sort(arr, base_index + 1, high)



def main():
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    # [6, 1, 2, 7, 3, 9]
    # print(quickSort(nums))
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


main()
