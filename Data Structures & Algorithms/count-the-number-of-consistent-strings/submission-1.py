class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=0

        for word in words:
            count=1
            for w in word:
                if w not in allowed:
                    count=0
                    break
            res+=count
        return res


