from src.mesher import MeshGenerator, Layer
import src.frontend as ui

def cone():
  layers = [Layer(1.0, 20), Layer(1.0, 1)]
  spacings = [2.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)

if __name__ == "__main__":
  cone()
