#  File: Hull.py

#  Description:

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Partner Name: Maxwell Kretschmer

#  Partner UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created:6/25/21

#  Date Last Modified:6/27/21



import sys
import math 

class Point(object):
    # constructor 
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    # prints point as a string 
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    # calculates the distance between two points  
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    # equality test of two points 
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))
    
    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y > other.y)
        return (self.x > other.x)
    
    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
        else:
            return (self.y >= other.y)
        return (self.x >= other.x)

# determines the determinant for three points (p, q, r)
def determinant(p, q, r):
    p = Point(p[0], p[1])
    q = Point(q[0], q[1])
    r = Point(r[0], r[1])
    return (p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y* p.x)

def convex_hull(sorted_points):
    
    # adds first two points to upper_hull list 
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    # adds points to upper_hull, removing 2nd points if not right turn 
    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while (len(upper_hull) >= 3):
            if (determinant(upper_hull[-1], upper_hull[-2], upper_hull[-3]) <= 0):
                del upper_hull[-2]
            else:
                break 

    # adds last two points to lower_hull list 
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    # adds points to lower_hull, removing 2nd points if not right turn 
    for j in range(len(sorted_points)-3, -1, -1):
        lower_hull.append(sorted_points[j])
        while (len(lower_hull) >= 3):
            if (determinant(lower_hull[-1], lower_hull[-2], lower_hull[-3]) <= 0):
                del lower_hull[-2]
            else:
                break

    # removes duplicate points from lower_hull that could be in upper_hull
    del lower_hull[0]
    del lower_hull[-1]

    # joins upper_hull and lower_hull 
    convex_hull_points = upper_hull + lower_hull

    return convex_hull_points

def area_enclosed(convex_points):
    '''
    use determinant formula to find area. 
    area = (1/2) * abs (det)
    '''
    return 100.12


def main():
    #READ IN DATA
    '''
    unformatted_inList = sys.stdin.readlines()
    tempList = [entry.strip().strip("\n") for entry in unformatted_inList]

    num_points = int(tempList[0])

    del tempList[0]

    inList = [line.split("\t") for line in tempList]

    formatted_inList = [ [int(line[0].strip()), int(line[1].strip())] for line in inList]
    formatted_inList = sorted(formatted_inList, key = lambda x: x[0])
    '''
    formatted_inList = [[-100, -33], [-96, 77], [-96, -82], [-95, -98], [-94, 22], [-93, 80], 
    [-90, 68], [-81, 80], [-80, 28], [-80, -39], [-79, 48], [-78, -64], [-75, -88], [-72, -45], 
    [-71, -50], [-69, 67], [-65, 50], [-64, -28], [-62, -60], [-62, 71], [-60, 8], [-59, 87], 
    [-54, 40], [-54, -42], [-51, -22], [-46, -98], [-46, -34], [-45, 80], [-44, -28], [-44, 16], 
    [-42, -41], [-41, 54], [-39, 24], [-34, -67], [-33, 21], [-32, -16], [-30, 55], [-27, -5], 
    [-27, 99], [-25, -1], [-23, -40], [-22, 26], [-19, 34], [-17, -17], [-15, -99], [-14, 40], 
    [-7, 65], [-4, -47], [1, 48], [5, -53], [7, 18], [9, 79], [18, 72], [20, -49], [21, -40], 
    [24, -33], [25, 100], [25, -9], [30, -89], [32, 90], [35, -41], [36, 63], [39, 82], [41, 18], 
    [41, -39], [43, -8], [45, 19], [46, 34], [46, 20], [47, -16], [55, -95], [55, -48], [55, -72], 
    [56, 67], [58, -2], [60, -63], [60, 89], [60, 28], [67, 50], [69, -98], [70, 4], [70, 68], [76, -73], 
    [77, 94], [78, 7], [80, 75], [81, 23], [81, -32], [84, 93], [84, -6], [84, -17], [85, 38], [86, 37], 
    [93, -28], [93, -42], [94, 26], [95, 14], [98, -83], [98, 0], [100, 26]]

    #RUN CONVEX_HULL
    convex_hull_points = convex_hull(formatted_inList)

    #FORMAT AND PRINT
    print("Convex Hull")
    for line in convex_hull_points:
        print(tuple(line))
    
    print()
    print("Area of Convex Hull = {:.1f}".format(area_enclosed(convex_hull_points)))

if __name__ == "__main__":
  main()
