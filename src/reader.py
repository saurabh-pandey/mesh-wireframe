'''
Creates a mesh from file
'''

from src.mesher import Point, Mesh, Segment

def read(filename):
  with open(filename) as f:
    header = f.readline()
    num_coords, num_edges = [int(str_in) for str_in in header.split()]
    print(f"num_coords = {num_coords}, num_edges = {num_edges}")
    points = []
    for i in range(num_coords):
      a_coord = f.readline()
      x, y, z = [float(str_in) for str_in in a_coord.split()]
      points.append(Point(x,y,z))
    segments = []
    for i in range(num_edges):
      a_line = f.readline()
      begin_id, end_id = [int(str_in) for str_in in a_line.split()]
      segments.append(Segment(begin_id, end_id))
    return Mesh(points, segments)