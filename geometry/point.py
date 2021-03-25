class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y

    def __repr__(self):
        return "Point(%s, %s)" % (self.y, self.x) + ")"
