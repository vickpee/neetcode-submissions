class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rightPtr = len(numbers)
        leftPtr = 0
        unFound = True
        indices = []
        while unFound:
            if numbers[leftPtr] + numbers[rightPtr - 1] < target:
                leftPtr += 1
            elif numbers[leftPtr] + numbers[rightPtr - 1] > target:
                rightPtr -= 1
            else:
                indices.append(leftPtr + 1)
                indices.append(rightPtr)
                unFound = False
        
        return indices