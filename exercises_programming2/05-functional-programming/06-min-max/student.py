def closest(points, target_point):
    return min(points, key=lambda point: distance(point, target_point))

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5