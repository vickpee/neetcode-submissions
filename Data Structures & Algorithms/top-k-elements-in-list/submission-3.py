class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #paired list, will have [[int, count], [int2, count2]]
        #to sort, use .sort(key=lambda item: item[1])
        allCount = []

        nums.sort()

        previous = nums[0]
        count = 1
        if len(nums) > 1:
            for index in range(1, len(nums)):
                if nums[index] == previous:
                    count += 1
                else:
                    allCount.append([previous, count])
                    count = 1
                    previous = nums[index]
                if index == len(nums) - 1:
                        allCount.append([previous, count])
        else:
            allCount.append([previous, count])

        allCount.sort(key=lambda item: item[1], reverse=True)

        onlyValue = [sublist[0] for sublist in allCount]

        return onlyValue[:k]