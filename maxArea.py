def maxArea(heights):
    left = 0
    right = len(heights) - 1
    max_area = min(heights[left], heights[right]) * (right - left)

    while left < right:
        if heights[left] < heights[right]:
            left += 1
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
        else:
            right -= 1
            max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
    return max_area
print(maxArea([1,8,6,2,5,4,8,3,7]))