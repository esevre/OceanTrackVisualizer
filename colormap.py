#
#  Custom Colormap and related functions
#
import numpy as np


class ColorPoint:
    def __init__(self, val : float, r : float, g : float, b : float, a : float = 0):
        self.val = val
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.a = float(a)

    def __str__(self):
        return "val(%3.2f), (r,g,b,a) : %3.2f, %3.2f, %3.2f, %3.2f" % (self.val, self.r, self.g, self.b, self.a)


class ColorMap:
    def __init__(self, min : float, max : float):
        self.min = float(min)
        self.max = float(max)
        self.minColorPoint = ColorPoint(min, 0, 0, 0)
        self.maxColorPoint = ColorPoint(max, 1, 1, 1)
        self.color_points = [self.minColorPoint, self.maxColorPoint]
        self.tolerance = 1e-6

    def set_min(self, r : float, g : float, b : float, a : float = 1):
        self.color_points[0] = ColorPoint(self.min, r, g, b, a)
        self.minColorPoint = ColorPoint(self.min, r, g, b, a)

    def set_max(self, r : float, g : float, b : float, a : float = 1):
        self.color_points[-1] = ColorPoint(self.max, r, g, b, a)
        self.maxColorPoint = ColorPoint(self.max, r, g, b , a)

    def set_midpoint(self, r : float, g : float, b : float, a : float = 1):
        midpoint = 0.5 * (self.max + self.min)
        self.add_color_point(midpoint, r, g, b, a)

    def add_color_point(self, val : float, r : float, g : float, b : float, a : float = 1):
        # Check for a new min
        if (val < self.min):
            self.min = val
            self.color_points.insert(0, ColorPoint(val, r, g, b, a))
            return
        # Check for a new max
        if (val > self.max):
            self.max = val
            self.color_points.append(ColorPoint(val, r, g, b, a))
            return
        # Search for the index we want to place a new color node between
        for index, cp in enumerate(self.color_points):
            # Check if the current index is being replaced
            if (np.fabs(cp.val - val) < self.tolerance):
                self.color_points[index] = ColorPoint(val, r, g, b, a)
                return
            # Check if the data should be inserted before the current index:
            if (val < cp.val):
                self.color_points.insert(index, ColorPoint(val, r, g, b, a))
                return
        # It should not reach this point !
        print("invalid entry in colormap object")

    def get_color(self, val : float) -> ColorPoint:

        if val <= self.min:
            return self.minColorPoint
        if val >= self.max:
            return self.maxColorPoint
        id = 0
        for index, cp in enumerate(self.color_points):
            if val < cp.val:
                id = index
                break
        p1 = self.color_points[id - 1]
        p2 = self.color_points[id]
        w1 = (p2.val - val) / (p2.val - p1.val)
        w2 = 1.0 - w1

        r = w1 * p1.r + w2 * p2.r
        g = w1 * p1.g + w2 * p2.g
        b = w1 * p1.b + w2 * p2.b
        a = w1 * p1.a + w2 * p2.a

        return ColorPoint(val, r, g, b, a)

    def get_color_tuple(self, val : float):
        color = self.get_color(val)
        return (color.r, color.g, color.b, color.a)




