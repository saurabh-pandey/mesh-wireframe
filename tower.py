from src.mesher import MeshGenerator, Layer
import src.frontend as ui

if __name__ == "__main__":
  layers = [Layer(1.0, 25), Layer(0.75, 25), Layer(0.5, 25), Layer(0.25, 25), Layer(0.1, 25), Layer(0.1, 1)]
  spacings = [0.25, 0.5, 1.0, 1.5, 2.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)
  