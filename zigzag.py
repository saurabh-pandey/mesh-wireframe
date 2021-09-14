from src.mesher import MeshGenerator, Layer
import src.frontend as ui

if __name__ == "__main__":
  odd_layer = Layer(1.0, 25)
  even_layer = Layer(1.0, 25, (1.0, 0.0))
  layers = [odd_layer, even_layer, odd_layer, even_layer, odd_layer, even_layer]
  spacings = [1.0, 1.0, 1.0, 1.0, 1.0]
  mesh = MeshGenerator(layers, spacings).generate()
  ui.draw(mesh)
  