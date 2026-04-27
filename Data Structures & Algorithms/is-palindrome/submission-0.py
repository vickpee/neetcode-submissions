class Solution:
    def isPalindrome(self, s: str) -> bool:
        listy = []
        for char in s:
            if char.isalnum():
                listy.append(char.lower())
        
        if listy == listy[::-1]:
            return True
        else:
            return False