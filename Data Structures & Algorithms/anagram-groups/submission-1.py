class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for string in strs:
            grams = []
            grams.append(string)
            for string2 in strs[strs.index(string) + 1:]:
                if sorted(string) == sorted(string2):
                    grams.append(string2)
                    strs.pop(strs.index(string2, strs.index(string) + 1))
            output.append(grams)

        return output