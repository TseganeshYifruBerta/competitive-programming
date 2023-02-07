class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        anticlockwise = ['N', 'W', 'S', 'E']
        clockwisee = ['N', 'E', 'S', 'W']
        
        counterclockwise_ = instructions.count('L')
        clockwise_ = instructions.count('R')
        
        
        direction = counterclockwise_ % 4
        direction = (clockwisee.index(anticlockwise[direction]) + clockwise_) % 4
        
        
        counter = {
            (0, 1) : (-1, 0),
            (-1, 0) : (0, -1),
            (0, -1) : (1, 0),
            (1, 0) : (0, 1)
        }
        
        clockwise = {
            (0, 1) : (1, 0),
            (1, 0) : (0, -1), 
            (0, -1) : (-1, 0), 
            (-1, 0) : (0, 1)
        }
        
        position = [0, 0]
        prev = [0, 1]
        for inst in instructions:
            x, y = position
            x_, y_ = prev
            if inst == 'G':
                position = [x_ + x, y_ + y]
                
            if inst == 'L':
                prev = counter[(x_, y_)]
                
            if inst == 'R':
                prev = clockwise[(x_, y_)]
                
        if position != [0, 0] and clockwisee[direction] == 'N':
            return False
        return True
                
                
        
        