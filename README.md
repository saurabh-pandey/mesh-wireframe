Steps to get it to work (on Linux):
```
1. git clone https://github.com/saurabh-pandey/mesh-wireframe.git
2. cd mesh-wireframe
3. python3 -m venv venv/
4. source venv/bin/activate
5. pip install -r requirements.txt
```
Now try:
```
python3 cone.py
```

and it should show the following:

![Cone](screenshots/cone.png?raw=true)

NOTE:
* Use **Pause/Continue** at the top to pause/continue the animation
* Use **Slider** at the bottom to increase/decrease the frame rate

Some sample run commands:
```
python3 cube.py
python3 cylinder.py
python3 invert.py
python3 pyramid.py
python3 tower.py
python3 zigzag.py
```
Some screenshots:

![Zigzag](screenshots/zigzag.png?raw=true)
![Invert](screenshots/invert.png?raw=true)