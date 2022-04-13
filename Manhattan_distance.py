class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        self.points = points
        
        distance = float('inf')
        steps = -1
        
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                d = abs(x-points[i][0]) + abs(y-points[i][1])
                if d < distance:
                    distance, steps = d, i
        return steps