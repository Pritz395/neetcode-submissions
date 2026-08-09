class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0

        for word in words:
            flag=1
            for w in word:
                if w not in allowed:
                    flag=0
                    break
            res+=flag
        return res
        