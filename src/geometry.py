'''
This file contains geometry primitives
'''

import math

class XYPoint:
  '''
  Point in XY plane
  '''
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y


class Layer:
  '''
  Represents a layer in the mesh.
  Assumptions:
  1. Always in XY plane
  2. Basically a circle with an approximation using N points
  '''
  def __init__(self, radius, num_pts, origin = (0.0, 0.0)) -> None:
    '''
    Construct a Layer (truly a Circle) using some radius and number of points to approximate it.
    Optionally, pass an origin
    NOTE: When num_pts is 1 this degenerates to a point at origin and any value of radius is
    ignored
    '''
    assert num_pts > 0
    if num_pts > 1:
      assert radius > 0
    
    self.radius = radius
    self.num_pts = num_pts
    self.origin = XYPoint(origin[0], origin[1])
    self.vertices = []
    if num_pts == 1:
      self.vertices = [self.origin]
    else:
      theta = 2*math.pi/num_pts
      for i in range(num_pts):
        x = self.origin.x + radius*math.cos(i*theta)
        y = self.origin.y + radius*math.sin(i*theta)
        self.vertices.append(XYPoint(x, y))
