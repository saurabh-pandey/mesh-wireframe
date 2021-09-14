from src.geometry import Layer


class Point:
  '''
  A point in 3D mesh
  '''
  def __init__(self, x, y, z) -> None:
    self.x = x
    self.y = y
    self.z = z

class Segment:
  '''
  A segment in 3D mesh formed from 2 points
  '''
  def __init__(self, begin_coord_id, end_coord_id) -> None:
    self.begin = begin_coord_id
    self.end = end_coord_id


class Mesh:
  '''
  A 3D mesh which a collection of points and segements connecting those points
  '''
  def __init__(self, points = [], segments = []) -> None:
    self.points = points
    self.segments = segments


class MeshGenerator:
  '''
  Generates a mesh given a layers (in XY plane) and spacing list to extrude it
  Assuption:
  1. Spacing is spacing between the layers, thus we need one less
  2. All layers have equal number of points or if unequal then one has single point
  '''
  def __init__(self, layers, spacings) -> None:
    self.num_layers = len(layers)
    self.num_spacings = len(spacings)
    assert (self.num_layers - self.num_spacings) == 1, "Spacing should be strictly one less than Layers"
    assert self.num_layers > 0, "Empty Layers not allowed"
    for i in range(self.num_layers - 1):
      if layers[i].num_pts != layers[i + 1].num_pts:
        assert (layers[i].num_pts == 1) or (layers[i + 1].num_pts == 1), f"Unequal layers found between {i} and {i + 1}"
    self.layers = layers
    self.spacings = spacings
    
  
  def generate(self):
    mesh = Mesh()
    # Fill points
    self.fill_points(mesh)
    # Fill segments within the layer
    self.fill_layer_segments(mesh)
    # Fill segments between two adjacent layers
    self.fill_inter_layer_segments(mesh)
    return mesh
  
  def fill_points(self, mesh):
    z = 0.0
    for i in range(self.num_layers):
      for v in self.layers[i].vertices:
        mesh.points.append(Point(v.x, v.y, z))
      if i < self.num_spacings:
        z += self.spacings[i]
  
  
  def fill_layer_segments(self, mesh):
    pt_counter = 0
    for i in range(self.num_layers):
      layer_num_pts = self.layers[i].num_pts
      # Layer with single point has no segments in the layer itself
      if layer_num_pts > 1:
        bounds = (pt_counter, pt_counter + layer_num_pts)
        for i in range(bounds[0], bounds[1] - 1):
          mesh.segments.append(Segment(i , i + 1))
        mesh.segments.append(Segment(bounds[1] - 1 , bounds[0]))
      pt_counter += layer_num_pts
  
  
  def fill_inter_layer_segments(self, mesh):
    pt_counter = 0
    for i in range(self.num_layers - 1):
      from_layer = self.layers[i]
      to_layer = self.layers[i + 1]
      if from_layer.num_pts != to_layer.num_pts:
        if from_layer.num_pts == 1:
          for i in range(to_layer.num_pts):
            mesh.segments.append(Segment(pt_counter , pt_counter + i + 1))
        elif to_layer.num_pts == 1:
          for i in range(from_layer.num_pts):
            mesh.segments.append(Segment(pt_counter + i, pt_counter + from_layer.num_pts))
      else:
        for i in range(from_layer.num_pts):
          mesh.segments.append(Segment(pt_counter + i, pt_counter + from_layer.num_pts + i))
      pt_counter += from_layer.num_pts
