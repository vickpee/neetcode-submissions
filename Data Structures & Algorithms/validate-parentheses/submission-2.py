class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        chars = []
        for i in range(len(s)):
            if s[i] in opening:
                chars.append(s[i])
            else:
                if len(chars) == 0:
                    return False
                elif opening[closing.index(s[i])] != chars[-1]:
                    return False
                else:
                    chars.pop()
        if len(chars) == 0:
            return True
        else:
            return False