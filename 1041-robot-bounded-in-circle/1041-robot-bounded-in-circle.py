class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        counter = {
            (0, 1) : (-1, 0, 'W'),
            (-1, 0) : (0, -1, 'S'),
            (0, -1) : (1, 0, 'E'),
            (1, 0) : (0, 1, 'N')}
        
        clockwise = {
            (0, 1) : (1, 0, 'E'),
            (1, 0) : (0, -1, 'S'), 
            (0, -1) : (-1, 0, 'W'), 
            (-1, 0) : (0, 1, 'N')}
        
        position = [0, 0]
        prev = [0, 1, 'N']
        
        for inst in instructions:
            x, y = position
            x_, y_, pos = prev
            if inst == 'G':
                position = [x_ + x, y_ + y]
                
            if inst == 'L':
                prev = counter[(x_, y_)]
                
            if inst == 'R':
                prev = clockwise[(x_, y_)]
                
        
        if position != [0, 0] and prev[2] == 'N':
            return False
        return True
                
                
        
        