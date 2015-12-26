# encoding: utf-8

from __future__ import division

tri = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]


class Path:
    def __init__(self, first_x=None, first_y=None):
        if first_x is None:
            self.points = []
        else:
            self.points = [(first_x, first_y)]

    def with_point(self, x, y):
        p = Path()
        p.points = self.points + [(x, y)]
        return p

    def last_point(self):
        return self.points[-1]

    def __repr__(self):
        return 'Path=' + repr(self.points)

    def value(self):
        result = 0
        for x, y in self.points:
            result += tri[y][x]
        return result


def fn(plist):
    result = []
    for path in plist:
        x, y = path.last_point()
        result.append(path.with_point(x + 1, y + 1))
        result.append(path.with_point(x, y + 1))
    return result


path_list = [Path(0, 0)]
for y in range(len(tri) - 1):
    path_list = fn(path_list)

values = []
for path in path_list:
    values.append(path.value())

print max(values)
