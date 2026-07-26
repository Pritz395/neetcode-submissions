class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        dup=set(nums)

        for num in nums:
            if num-1 not in dup:
                length=0
                while length+num in dup:
                    length+=1
                longest=max(longest,length)
        return longest