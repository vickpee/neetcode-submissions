class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        uniqueNums = []

        if len(nums) > 0:
            longest = -1
            current = 1
            nums.sort()
            for num in nums:
                if num not in uniqueNums:
                    uniqueNums.append(num)
            previousNum = uniqueNums[0]

            for item in uniqueNums[1:]:
                if item == previousNum + 1:
                    current += 1
                    previousNum = item
                else:
                    longest = max(longest, current)
                    current = 1
                    previousNum = item
            
            if current > longest:
                        longest = current
                        current = 1
            
            return longest
    
        else:
            return 0
