class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newarr=[]

        for x in arr2:
            for y in arr1:
                if x==y:
                    newarr.append(y)

        empty=[]

        for x in arr1:
            if x not in arr2:
                empty.append(x)
        empty.sort()
                
        return newarr+empty