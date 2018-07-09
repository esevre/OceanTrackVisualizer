#
#  Compute derivatives for 2D data
#
#
from typing import List
import numpy as np
import scipy as sci
import numpy.linalg as lin

#
#  Erik's custom function headers
#
import processFile as pf


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


#
#  Object to hold track data including:
#    pts for location of observed data
#    corrected points for line analyzed data
#    direction of the line of motion
#      (initially from data, better estimates to come later)
#
#  todo: update track to simplify a lot of the work for data analysis
class track:
    def __init__(self, filename : str):
        self.pts = []
        self.corrected_pts = []
        self.direction = []
        pass


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
    for i, pt in enumerate(pt_array):
        results[i] = project_point_on_line(pt, line_a, line_b)
    return results


def length2d(x, y) -> float:
    return np.sqrt(x**2+y**y)


def distance_between_p1p2(x1, y1, x2, y2) -> float:
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)


def dAge_dPoint(age1 : float, age2 : float, point1 : point, point2 : point) -> float:
    value = (age2-age1) / (distance_between_p1p2(point1.x, point1.y, point2.x, point2.y))
    return value


def generate_spreading_rates(ages : List[float], points : List[point]) -> List[float]:
    size = len(ages) - 1
    spreading_rates = []
    for i in range(size):
        dAge_dPosition = dAge_dPoint(ages[i], ages[i+1], points[i], points[i+1])
        spreading_rates.append(dAge_dPosition)
    return np.array(spreading_rates)


def generate_points_from_arrays(x : List[float], y : List[float]) -> List[point] :
    point_array = []
    for i in range(len(x)):
        point_array.append(point(x[i], y[i]))
    return point_array


def generate_xy_from_points(points : List[point]):
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i].x)
        y.append(points[i].y)
    return x, y


def map_xy_to_line(x : List[float],
                   y : List[float]):
    pts = generate_points_from_arrays(x, y)
    pts = project_points_on_line(pts, pts[0], pts[-1])
    return generate_xy_from_points(pts)


def x_y_from_data(data : List[point]):
    x = []
    y = []
    for pt in data:
        x.append(pt.x)
        y.append(pt.y)
    return x, y


def generate_plotable_data(filename : str):
    """
    Generate x, y, age, spreading rate data from tabbed file

    :param filename: path to file
    :return: x, y, ages, spreading_rates
    """
    header, data = pf.get_data_from_tab_separated_file(filename)
    x = np.array([x for x, y, age in data])
    y = np.array([y for x, y, age in data])

    ages = np.array([age for x, y, age in data])

    pts = []
    for i in range(len(x)):
        pts.append(point(x[i], y[i]))

    spreading_rates = generate_spreading_rates(ages, pts)
    return x, y, ages, spreading_rates


#
#  Get min-avg-max from single input file
#
def get_min_avg_max_from_file(filename : str):
    x, y, _, _ = generate_plotable_data(filename)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    xavg = (xmax-xmin)/2.0
    yavg = (ymax-ymin)/2.0
    return xmin, xavg, xmax, ymin, yavg, ymax


def get_min_avg_max_from_file_list(files : [str]):
    xmin = None
    xmax = None
    ymin = None
    ymax = None

    for file in files:
        if xmin is None:
            xmin, _, xmax, ymin, _, ymax = get_min_avg_max_from_file()
        else:
            x0, _, x2, y0, _, y2 = get_min_avg_max_from_file(file)
            if x0 < xmin:
                xmin = x0
            if x2 > xmax:
                xmax = x2
            if y0 < ymin:
                ymin = y0
            if y2 > ymax:
                ymax = y2

    xavg = (xmax-xmin)/2.0
    yavg = (ymax-ymin)/2.0
    return xmin, xavg, xmax, ymin, yavg, ymax

