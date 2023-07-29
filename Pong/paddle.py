class Paddle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    
    def move(self, mx, my, dt):
        self.x += mx * dt
        self.y += my * dt