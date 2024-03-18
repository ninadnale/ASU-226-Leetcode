class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        prevLast = points[0][1]
        
        for i in range(1, len(points)):
            if(prevLast>=points[i][0]):
                if(prevLast>points[i][1]):
                    prevLast = points[i][1]
            else:
                prevLast = points[i][1]
                arrows += 1

        return arrows