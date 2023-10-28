def setup():
     size (1000 ,1000)
def draw():
    global q
    frameRate (10)
    background (200 ,0 ,100)
    q=random(75)
    ellipse (500 ,500 ,q ,q)
