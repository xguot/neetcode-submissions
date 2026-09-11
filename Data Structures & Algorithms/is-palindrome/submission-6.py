class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        if not s:
            return True

        p = len(s) - 1
        for i in range(0, int(len(s)/2 + 1)):
            if s[i] != s[p-i]:
                return False

        return True
