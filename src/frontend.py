import src.reader as reader
from src.mesher import MeshGenerator, Layer

from vpython import *

class FrontEnd:
  '''
  Main UI to show the mesh creation as animation
  '''
  def __init__(self) -> None:
    # Set camera
    scene.forward = vec(0,1,-1)
    
    # UI title
    scene.title = "Meshing Animation\n"
    
    # Pause/Continue button
    self.running = True
    def Run(b):
      self.running = not self.running
      if self.running:
        b.text = "Pause"
      else:
        b.text = "Continue"
    button(text="Pause", pos=scene.title_anchor, bind=Run)

    # Usage guide
    scene.caption = """
    1. To rotate "camera", drag with right button or Ctrl-drag.
    2. To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
    3. To pan left/right and up/down, Shift-drag.
    4. Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
    \nAnimation speed:\n
    """

    # Animate speed slider
    def setspeed(s):
        wt.text = '{:1.2f}'.format(s.value)
    self.sl = slider(min=0.5, max=100.0, value=10, length=220, bind=setspeed, right=15)
    wt = wtext(text='{:1.2f}'.format(1.0/self.sl.value))
    scene.append_to_caption(' frames/s\n')
  

  def render(self, mesh):
    '''
    Render a mesh in the above front-end
    '''
    curves = []
    i = 0
    while i  < len(mesh.segments):
      sleep(1.0/self.sl.value)
      if self.running:
        seg = mesh.segments[i]
        start_pt = mesh.points[seg.begin]
        end_pt = mesh.points[seg.end]
        start = vector(start_pt.x, start_pt.y, start_pt.z)
        end = vector(end_pt.x, end_pt.y, end_pt.z)
        curves.append(curve(start, end))
        i += 1
      else:
        continue
    return curves

  
  def hide(self, curves):
    '''
    Hide mesh
    '''
    for c in curves:
      c.visible = False

  
  def animate(self, curves):
    '''
    Animation that hides the mesh and then makes it visible in an infinte loop
    '''
    while True:
      sleep(1.0/self.sl.value)
      self.hide(curves)
      i = 0
      while i  < len(curves):
        sleep(1.0/self.sl.value)
        if self.running:
          curves[i].visible = True
          i += 1
        else:
          continue


def draw(mesh):
  '''
  Draw a mesh
  '''
  frontend = FrontEnd()
  curves = frontend.render(mesh)
  frontend.animate(curves)


def draw_from_file(filename):
  '''
  Draw a mesh from file
  '''
  mesh = reader.read(filename)
  draw(mesh)
