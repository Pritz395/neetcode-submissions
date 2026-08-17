class Solution:
    def maxScore(self, s: str) -> int:
        sum0=s.count('1')
        maxval=0

        for i in range(len(s)-1):
            if s[i]=='0':
                sum0+=1
            else:
                sum0-=1
            maxval=max(maxval,sum0)
        return maxval