# f=10
# z=990
# def setup():
#     size (1000 ,1000)
# def draw():
#     global f ,z
#     background (200 ,0 ,100)
#     fill (234 ,23 ,34)
#     ellipse (f ,500 ,40 ,40)
#     fill (56 ,231 ,177)
#     ellipse (z ,500 ,40 ,40)
#     f=f+1
#     z=z-1



def setup():
    size (1000 ,1000)
    background (0 ,0 ,0)
def draw():
     global s ,p ,q
     s=random(1000)
     p=random(1000)
     q=random(1,5)
     stroke (random(200,255),random(200,255),random(200,255))
     strokeWeight (q)
     point (p ,s)
