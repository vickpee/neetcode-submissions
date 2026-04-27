class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            daysWarmer = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    daysWarmer = j - i
                    break
            result.append(daysWarmer)

        return result