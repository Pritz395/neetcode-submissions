class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        emptyarr=[]

        for x in arr2:
            for y in arr1:
                if x==y:
                    emptyarr.append(x)

        remaining=[]

        for x in arr1:
            if x not in arr2:
                remaining.append(x)
        
        remaining=sorted(remaining)

        return emptyarr+remaining