class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
    
    def move(mx, my, dt):
        self.x += mx * dt
        self.y += my * dt