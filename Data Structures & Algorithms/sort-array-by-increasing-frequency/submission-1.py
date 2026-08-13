class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)

        return sorted(nums, key=lambda n: (count[n], -n))


