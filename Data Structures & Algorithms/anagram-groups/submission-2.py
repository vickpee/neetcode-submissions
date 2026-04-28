class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        hashy = {}

        for item in strs:
            sorty = "".join(sorted(item))

            if sorty not in hashy:
                hashy[sorty] = []

            hashy[sorty].append(item)
        
        return list(hashy.values())
