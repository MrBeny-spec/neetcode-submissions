class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s)
        news = ""
        for char in s:
            if char.isalnum():
                news += char 
        ans = news.lower()
        if ans == ans[::-1]:
            return True
        return False