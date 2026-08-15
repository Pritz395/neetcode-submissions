class Solution:
    def maxScore(self, s: str) -> int:
        sumO = s.count('1')
        maxVal=0
        for i in range(len(s)-1):
            if s[i] == '0':
                sumO+= 1
            else:
                sumO-= 1
            maxVal=max(maxVal,sumO)
        return maxVal
            