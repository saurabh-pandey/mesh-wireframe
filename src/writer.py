'''
Write a mesh to the file
'''

def write(mesh, filename):
  with open(filename, 'w') as f:
    f.write(f"{len(mesh.points)} {len(mesh.segments)}\n")
    for pt in mesh.points:
      f.write(f"{pt.x} {pt.y} {pt.z}\n")
    for seg in mesh.segments:
      f.write(f"{seg.begin} {seg.end}\n")