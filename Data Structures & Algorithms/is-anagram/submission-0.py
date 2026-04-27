class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        charsS = {}
        charsT = {}

        if len(s) == len(t):
            for i in s:
                if i not in charsS:
                    charsS[i] = 1
                else:
                    charsS[i] += 1
            for j in t:
                if j not in charsT:
                    charsT[j] = 1
                else:
                    charsT[j] += 1

            print(charsS)
            print(charsT)

            if charsS == charsT:
                return True

        return False