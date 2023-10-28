def setup():
     size (1000 ,1000)
def draw():
    global t ,q ,r ,u ,s ,J
    background (0 ,150 ,0)
    r=random(255)
    u=random(255)
    t=random(255)
    q=random(50)
    J=random(1000)
    s=random(1000)
    stroke (t ,r ,u)
    strokeWeight (q)
    line (500 ,500 ,s ,J)
