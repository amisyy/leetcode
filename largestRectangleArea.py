class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area,h*w)
            stack.append(i)
        return max_area


u = Solution()



test = [
    [2,1,5,6,2,3],
    [3,1,3,2,2,0]
]
for x in test:
    print(u.largestRectangleArea(x))




