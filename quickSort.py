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


def main():
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(quickSort(nums))

main()