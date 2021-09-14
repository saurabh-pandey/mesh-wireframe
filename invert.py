from src.mesher import MeshGenerator, Layer
import src.frontend as ui

if __name__ == "__main__":
  l0 = Layer(1.0, 25)
  l1 = Layer(0.75, 25)
  l2 = Layer(0.5, 25)
  l3 = Layer(0.25, 25)
  l4 = Layer(0.0, 1)
  layers = [l0, l1, l2, l3, l4, l3, l2, l1, l0]
  spacings = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)
  