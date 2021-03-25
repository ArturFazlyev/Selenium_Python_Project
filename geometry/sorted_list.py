from geometry.point import Point

l1 = [Point(5, 2), Point(2, 3), Point(3, 6)]

l = list(map(lambda i: Point(i, i * i), range(-5, 6)))
n = list(filter(lambda p: p.x > 0, l))
print(n)
m = map(lambda r: r * r, range(0, 5))
numbers = [10, 15, 21, 33, 42, 55]
print(list(map(lambda x: x * 2 + 3, numbers)))
print(list(m))
print(l)

l2 = sorted(l1, key=lambda p: p.x)
