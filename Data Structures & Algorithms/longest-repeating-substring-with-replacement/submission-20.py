class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        longest=0
        i=0
        count={}

        for j in range(len(s)):
            count[s[j]]=1+count.get(s[j],0)
            longest=max(longest,count[s[j]])

            if (j-i+1)-longest>k:
                count[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res