class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allChar = []
        for i in nums:
            if i not in allChar:
                allChar.append(i)
            else:
                return True
        
        return False