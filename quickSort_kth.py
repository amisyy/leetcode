def quickSort(nums,k):
    length = len(nums)
    less = []
    more = []
    base = nums.pop()
    for i in nums:
        if i > base:
            more.append(i)
        else:
            less.append(i)
    less_length = len(less)
    if less_length > k:
        return quickSort(less, k)
    elif less_length < k-1:
        return quickSort(more, length-k-1)
    else:
        return base
def main():
    nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(quickSort(nums,6))
main()