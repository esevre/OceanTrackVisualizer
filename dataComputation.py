#
#  Compute derivatives for 2D data
#
#
from typing import List
import numpy as np
import scipy as sci
import numpy.linalg as lin

#
#  point
#
#  Lightweight class to do quick basic 2d vector operations
#
#  Operations defined:
#    pt0 = point()
#    pt1 = point(2, 3.14)
#    pt1 + pt2
#    pt1 - pt2
#
class point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def dot(self, pt):
        return self.x * pt.x + self.y * pt.y

    def len(self):
        return np.sqrt(self.dot(self))

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    def __add__(self, other):
        return point(other.x + self.x, other.y + self.y)

    def __sub__(self, other):
        return point(other.x - self.x, other.y - self.y)

    def __mul__(self, other):
        return point(self.x*other, self.y*other)

    def __rmul__(self, other):
        return point(self.x*other, self.y*other)


def project_point_on_line(pt: point, line_a: point, line_b: point):
    ln = line_b - line_a                          # compute direction vector
    ln = point(ln.x / ln.len(), ln.y / ln.len())  # normalize the vector

    m_pt = pt - line_a
    m_dot = -m_pt.dot(ln)  # / ln.dot(ln)
    m_dot_ln = m_dot * ln
    m_dot_ln_corrected = m_dot_ln + line_a
    return m_dot_ln_corrected                     # return the projection


def project_points_on_line(pt_array: List[point], line_a: point, line_b: point):
    results = pt_array
    # r = [project_point_on_line(pt, line_a, line_b) for pt in pt_array]
    for i, pt in enumerate(pt_array):
        results[i] = project_point_on_line(pt, line_a, line_b)
    return results


def length2d(x, y) -> float:
    return np.sqrt(x**2+y**y)


def distance_between_p1p2(x1, y1, x2, y2) -> float:
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)









