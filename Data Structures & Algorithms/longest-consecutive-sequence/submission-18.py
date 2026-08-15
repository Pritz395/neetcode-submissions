class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        empty=set(nums)

        for num in nums:
            if num-1 not in empty:
                length=0
                while length+num in empty:
                    length+=1
                longest=max(longest,length)
        return longest