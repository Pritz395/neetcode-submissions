class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y=0,0
        values={(0,0)}

        for directions in path:
            if directions=="N":
                y+=1
            elif directions=="S":
                y-=1
            elif directions=="W":
                x+=1
            elif directions=="E":
                x-=1

            if (x,y) in values:
                return True

            values.add((x,y))
        return False 
            
