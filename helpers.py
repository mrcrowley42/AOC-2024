class Vector2:
    def __init__(self,r,c):
        self.r, self.c = r, c
        
    def __add__(self, other):
        return Vector2(self.r + other.r, self.c + other.c)
    
    def location(self):
        return (self.r, self.c)   

directions = {"L": Vector2(0, -1), "R": Vector2(0, 1), "D": Vector2(-1, 0), "U": Vector2(1, 0)}

def rows_to_columns(rows):
    return list(map(list, zip(*rows)))