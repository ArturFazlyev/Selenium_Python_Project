from geometry.point import Point

l1 = [Point(5, 2), Point(2, 3), Point(3, 6)]

l2 = sorted(l1, key=lambda p: p.x)

print(l2)
