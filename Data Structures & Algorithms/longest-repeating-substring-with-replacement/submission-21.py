class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maximum=0
        res=0
        i=0

        for j in range(len(s)):
            count[s[j]]=1+count.get(s[j],0)
            maximum=max(maximum,count[s[j]])
            
            if (j-i+1)-maximum>k:
                count[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res


        