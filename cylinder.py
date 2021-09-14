from src.mesher import MeshGenerator, Layer
import src.frontend as ui

def cylinder():
  l = Layer(1.0, 20)
  layers = [l, l]
  spacings = [6.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)

if __name__ == "__main__":
  cylinder()
