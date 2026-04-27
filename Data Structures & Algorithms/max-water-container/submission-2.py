class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        largestWater = 0
        first = 0
        last = len(heights) - 1

        for i in range(len(heights) - 1):
            water = (last - first) * min(heights[first], heights[last])
            if largestWater < water:
                largestWater = water
            
            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1
        
        return largestWater