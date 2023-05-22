from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        if len(s) == 1:
            return 1
        dict = collections.Counter(s)
  
        for key, cnt in dict.items():
            if cnt % 2 == 0:
                answer += cnt
            else:
                answer += cnt - 1
        if len(s) > answer:
            return answer + 1
        else:
            return answer
