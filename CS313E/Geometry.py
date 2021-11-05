#  File: Geometry.py

#  Description:

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created:6/19/21

#  Date Last Modified:6/21/21

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return "({}, {}, {})".format(self.x, self.y, self.z)

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      return math.sqrt( ((self.x - other.x)**2) + ((self.y - other.y)**2) + ((self.z - other.z)**2) )

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      tol = 1.0e-6
      if (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol):
          return True
      else:
          return False

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.center = Point(x, y, z)
      self.radius = radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return "Center: {}, Radius: {}".format(self.center, self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return 4*math.pi*(self.radius**2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return (4/3)*math.pi*(self.radius**3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (p.distance(self.center)) < (self.radius)

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      return self.is_inside_point(other.center) and (self.center.distance(other.center) + other.radius) < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      diag = a_cube.side*(1/2)*math.sqrt(3)
      return self.is_inside_point(a_cube.center) and (self.center.distance(a_cube.center) + diag) < self.radius

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      diag = math.sqrt((a_cyl.radius**2)+(a_cyl.height*(1/2))**2)
      return self.is_inside_point(a_cyl.center) and (self.center.distance(a_cyl.center) + diag) < self.radius

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      return (not(self.is_inside_sphere(other))) and (not(self.radius + other.radius < self.center.distance(other.center)))

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      diag = a_cube.side*(1/2)*math.sqrt(3)
      _isOutside = self.radius + (a_cube.side/2) < self.center.distance(a_cube.center) and self.radius + diag < self.center.distance(a_cube.center)
      return (not(self.is_inside_cube(a_cube))) and (not _isOutside)

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      side = (2*self.radius)/math.sqrt(3)
      return Cube(self.center.x, self.center.y, self.center.z, side)

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.center = Point(x, y, z)
      self.side = side
      self.xmin = self.center.x - side/2
      self.xmax = self.center.x + side/2
      self.ymin = self.center.y - side/2
      self.ymax = self.center.y + side/2
      self.zmin = self.center.z - side/2
      self.zmax = self.center.z + side/2

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return "Center: {}, Side: {}".format(self.center, self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return 6 * (self.side**2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      return self.side**3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      diag = self.side*(1/2)*math.sqrt(3)
      return (p.distance(self.center)) < diag or (p.distance(self.center)) < (self.side/2)

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      return self.is_inside_point(a_sphere.center) and (self.center.distance(a_sphere.center) + a_sphere.radius) < (self.side/2)

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      diag_self = self.side*(1/2)*math.sqrt(3)
      diag_other = other.side*(1/2)*math.sqrt(3)
      return self.is_inside_point(other.center) and ((self.center.distance(other.center) + (other.side/2)) < (self.side/2) or (self.center.distance(other.center) + diag_other) < diag_self)

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      diag_self = self.side*(1/2)*math.sqrt(3)
      diag_other = math.sqrt((a_cyl.radius**2)+(a_cyl.height*(1/2))**2)
      return self.is_inside_point(a_cyl.center) and ((self.center.distance(a_cyl.center) + (a_cyl.radius)) < (self.side/2) or (self.center.distance(a_cyl.center) + diag_other) < diag_self)

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      self_diag = self.side*(1/2)*math.sqrt(3)
      other_diag = other.side*(1/2)*math.sqrt(3)
      _isOutside = (self.side/2) + (other.side/2) < self.center.distance(other.center) and self_diag + other_diag < self.center.distance(other.center)
      return (not(self.is_inside_cube(other))) and (not _isOutside)

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    # intersection will have 6 sides
        self.side_x1 = 0
        self.side_x2 = 0
        self.side_y1 = 0
        self.side_y2 = 0
        self.side_z1 = 0
        self.side_z2 = 0

        if self.does_intersect_cube(other):
            if self.xmin > other.xmin:
                self.side_x1 = self.xmin
            elif self.xmin < other.xmin: 
                self.side_x1 = other.xmin
            if self.xmax > other.xmax: 
                self.side_x2 = other.xmax
            elif self.xmax < other.xmax:
                self.side_x2 = self.xmax

            # finds the 2 y-faces of intersection 
            if self.ymin > other.ymin:
                self.side_y1 = self.ymin
            elif self.ymin < other.ymin: 
                self.side_y1 = other.ymin 
            if self.ymax < other.ymax:
                self.side_y2 = self.ymax
            elif self.ymax > other.ymax: 
                self.side_y2 = other.ymax 

            # finds the 2 z-faces of intersection 
            if self.zmin > other.zmin:
                self.side_z1 = self.zmin 
            elif self.zmin < other.zmin: 
                self.side_z1 = other.zmin 
            if self.zmax > other.zmax: 
                self.side_z2 = other.zmax
            elif self.zmax < other.zmax:
                self.side_z2 = self.zmax

        # determines the distance between faces to find volume 
        self.x_dimension = abs(self.side_x1 - self.side_x2)
        self.y_dimension = abs(self.side_y1 - self.side_y2)
        self.z_dimension = abs(self.side_z1 - self.side_z2)

        return float(self.x_dimension * self.y_dimension * self.z_dimension)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
        return Sphere(self.center.x, self.center.y, self.center.z, self.side/2)

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.center = Point(x, y, z)
      self.radius = radius
      self.height = height
      self.xmin = self.center.x - self.radius
      self.xmax = self.center.x + self.radius
      self.ymin = self.center.y - self.radius
      self.ymax = self.center.y + self.radius
      self.zmin = self.center.z - self.height
      self.zmax = self.center.z + self.height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return "Center: {}, Radius: {}, Height: {}".format(self.center, self.radius, self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return (2*math.pi*self.radius*self.height) + (2*math.pi*(self.radius**2))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return math.pi*(self.radius**2)*self.height

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return (p.x > self.xmin and p.x < self.xmax) and (p.y > self.ymin and p.y < self.ymax) and (p.z > self.zmin and p.z < self.zmax)

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      return (a_sphere.center.x - a_sphere.radius > self.xmin and a_sphere.center.x + a_sphere.radius < self.xmax) and (a_sphere.center.y - a_sphere.radius > self.ymin and a_sphere.center.y + a_sphere.radius < self.ymax) and (a_sphere.center.z - a_sphere.radius > self.zmin and a_sphere.center.z - a_sphere.radius < self.zmax)

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      return False

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
       diag_self = math.sqrt((self.radius**2)+(self.height*(1/2))**2)
       diag_other = math.sqrt((other.radius**2)+(other.height*(1/2))**2)
       return self.is_inside_point(other.center) and ((self.center.distance(other.center) + (other.radius)) < (self.radius) or (self.center.distance(other.center) + diag_other) < diag_self)

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
       diag_self = math.sqrt((self.radius**2)+(self.height*(1/2))**2)
       diag_other = math.sqrt((other.radius**2)+(other.height*(1/2))**2)
       _isOutside = self.radius + other.radius < self.center.distance(other.center) and diag_self + diag_other < self.center.distance(other.center)
       return (not(self.is_inside_cube(other))) and (not _isOutside)

def main():
    import sys
  # read data from standard input
    data_in_unformatted = sys.stdin.readlines()
    data_in = [entry.strip("\n").strip() for entry in data_in_unformatted]
    coords_Lst = [list(line.split("#"))[0].strip().split(' ') for line in data_in]
    
  # read the coordinates of the first Point p
    unformatted_pCoordsLst = coords_Lst[0]
    del coords_Lst[0]
    pCoordsLst = [float(coord) for coord in unformatted_pCoordsLst]
    
  # create a Point object 
    p = Point(pCoordsLst[0], pCoordsLst[1], pCoordsLst[2])

  # read the coordinates of the second Point q
    unformatted_qCoordsLst = coords_Lst[0]
    del coords_Lst[0]
    qCoordsLst = [float(coord) for coord in unformatted_qCoordsLst]

  # create a Point object 
    q = Point(qCoordsLst[0], qCoordsLst[1], qCoordsLst[2])

  # read the coordinates of the center and radius of sphereA
    unformatted_sphereACoordsLst = coords_Lst[0]
    del coords_Lst[0]
    sphereACoordsLst = [float(coord) for coord in unformatted_sphereACoordsLst]

  # create a Sphere object 
    sphereA = Sphere(sphereACoordsLst[0], sphereACoordsLst[1], sphereACoordsLst[2],sphereACoordsLst[3])

  # read the coordinates of the center and radius of sphereB
    unformatted_sphereBCoordsLst = coords_Lst[0]
    del coords_Lst[0]
    sphereBCoordsLst = [float(coord) for coord in unformatted_sphereBCoordsLst]

  # create a Sphere object
    sphereB = Sphere(sphereBCoordsLst[0], sphereBCoordsLst[1], sphereBCoordsLst[2],sphereBCoordsLst[3])

  # read the coordinates of the center and side of cubeA
    unformatted_cubeACoordsLst = coords_Lst[0]
    del coords_Lst[0]
    cubeACoordsLst = [float(coord) for coord in unformatted_cubeACoordsLst]

  # create a Cube object 
    cubeA = Cube(cubeACoordsLst[0], cubeACoordsLst[1], cubeACoordsLst[2], cubeACoordsLst[3])

  # read the coordinates of the center and side of cubeB
    unformatted_cubeBCoordsLst = coords_Lst[0]
    del coords_Lst[0]
    cubeBCoordsLst = [float(coord) for coord in unformatted_cubeBCoordsLst]

  # create a Cube object 
    cubeB = Cube(cubeBCoordsLst[0], cubeBCoordsLst[1], cubeBCoordsLst[2], cubeBCoordsLst[3])

  # read the coordinates of the center, radius and height of cylA
    unformatted_cylACoordsLst = coords_Lst[0]
    del coords_Lst[0]
    cylACoordsLst = [float(coord) for coord in unformatted_cylACoordsLst]

  # create a Cylinder object 
    cylA = Cylinder(cylACoordsLst[0], cylACoordsLst[1], cylACoordsLst[2], cylACoordsLst[3], cylACoordsLst[4])

  # read the coordinates of the center, radius and height of cylB
    unformatted_cylBCoordsLst = coords_Lst[0]
    del coords_Lst[0]
    cylBCoordsLst = [float(coord) for coord in unformatted_cylBCoordsLst]

  # create a Cylinder object
    cylB = Cylinder(cylBCoordsLst[0], cylBCoordsLst[1], cylBCoordsLst[2], cylBCoordsLst[3], cylBCoordsLst[4])

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    if p.distance(Point()) > q.distance(Point()):
        sys.stdout.write("Distance of Point p from the origin is greater than the distance of Point q from the origin\n")
    else:
        sys.stdout.write("Distance of Point p from the origin is not greater than the distance of Point q from the origin\n")
        

  # sys.stdout.write if Point p is inside sphereA
    if sphereA.is_inside_point(p):
        sys.stdout.write("Point p is inside sphereA\n")
    else:
        sys.stdout.write("Point p is not inside sphereA\n")
  # sys.stdout.write if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB):
        sys.stdout.write("sphereB is inside sphereA\n")
    else:
        sys.stdout.write("sphereB is not inside sphereA\n")
  # sys.stdout.write if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA):
        sys.stdout.write("cubeA is inside sphereA\n")
    else:
        sys.stdout.write("cubeA is not inside sphereA\n")
  # sys.stdout.write if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA):
        sys.stdout.write("cylA is inside sphereA\n")
    else:
        sys.stdout.write("cylA is not inside sphereA\n")

  # sys.stdout.write if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA):
        sys.stdout.write("sphereA does intersect sphereB\n")
    else:
        sys.stdout.write("sphereA does not intersect sphereB\n")
  # sys.stdout.write if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB):
        sys.stdout.write("cubeB does intersect sphereB\n")
    else:
        sys.stdout.write("cubeB does not intersect sphereB\n")
  # sys.stdout.write if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        sys.stdout.write("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA\n")
        
    else:
        sys.stdout.write("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA\n")

  # sys.stdout.write if Point p is inside cubeA
    if cubeA.is_inside_point(p):
        sys.stdout.write("Point p is inside cubeA\n")
    else:
        sys.stdout.write("Point p is not inside cubeA\n")
  # sys.stdout.write if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA):
        sys.stdout.write("sphereA is inside cubeA\n")
    else:
        sys.stdout.write("sphereA is not inside cubeA\n")
  # sys.stdout.write if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB):
        sys.stdout.write("cubeB is inside cubeA\n")
    else:
        sys.stdout.write("cubeB is not inside cubeA\n")
  # sys.stdout.write if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA):
        sys.stdout.write("cylA is inside cubeA\n")
    else:
        sys.stdout.write("cylA is not inside cubeA\n")
  # sys.stdout.write if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA):
        sys.stdout.write("cubeA does intersect cubeB\n")
    else:
        sys.stdout.write("cubeA does not intersect cubeB\n")
  # sys.stdout.write if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        sys.stdout.write("Intersection volume of cubeA and cubeB is greater than the volume of sphereA\n")
    else:
        sys.stdout.write("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA\n")
  # sys.stdout.write if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        sys.stdout.write("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA\n")
    else:
        sys.stdout.write("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA\n")
        
  # sys.stdout.write if Point p is inside cylA
    if cylA.is_inside_point(p):
        sys.stdout.write("Point p is inside cylA\n")
    else:
        sys.stdout.write("Point p is not inside cylA\n")
  # sys.stdout.write if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA):
        sys.stdout.write("sphereA is inside cylA\n")
    else:
        sys.stdout.write("sphereA is not inside cylA\n")
  # sys.stdout.write if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA):
        sys.stdout.write("cubeA is inside cylA\n")
    else:
        sys.stdout.write("cubeA is not inside cylA\n")
  # sys.stdout.write if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB):
        sys.stdout.write("cylB is inside cylA\n")
    else:
        sys.stdout.write("cylB is not inside cylA\n")
  # sys.stdout.write if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB):
        sys.stdout.write("cylB does intersect cylA\n")
    else:
        sys.stdout.write("cylB does not intersect cylA\n")

if __name__ == "__main__":
  main()