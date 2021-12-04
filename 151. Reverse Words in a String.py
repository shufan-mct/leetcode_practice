class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        reverse = reversed(splited)
        return ' '.join(reverse)
