class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s=s.split(" ")
        if len(pattern)!=len(s):
            return False

        charmap={}
        wordmap={}

        for c,w in zip(pattern,s):
            if c in charmap and charmap[c]!=w:
                return False
            if w in wordmap and wordmap[w]!=c:
                return False
            charmap[c]=w
            wordmap[w]=c

        return True
            
