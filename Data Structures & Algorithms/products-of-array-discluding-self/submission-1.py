class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sizeNums = len(nums)
        output = [1 for item in nums]

        for i in range(sizeNums):
            for j in range(sizeNums):
                if i != j:
                    output[j] *= nums[i]
        
        return output