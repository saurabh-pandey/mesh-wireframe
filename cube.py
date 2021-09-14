from src.mesher import MeshGenerator, Layer
import src.frontend as ui

def cube():
  layers = [Layer(1.0, 4), Layer(1.0, 4)]
  spacings = [2.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)

if __name__ == "__main__":
  cube()
