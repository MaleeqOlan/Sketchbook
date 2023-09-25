def setup():
     global x
     global f
     global y
     global p
     global c
     background(0)
     x = width / 2
     f = height / 2
     y = height/ -50
     p = width/ 10
     c = height/ 50
     size(750,750)
     
x= 0
def draw():
    global x
    global f
    global y
    global p
    global c
    background(255,100,100)
    fill(255,255,250)
    circle(x,f,200)
    fill(150,250,250)
    circle(x,y,200)
    fill(100,400,600)
    circle(p,f ,250)
    fill(150,225,250)
    circle(c,y,-200)
    fill(250,255,120)
    x= x + 1
    f= f + 1
    y= y - 1
    p= p - 1
    c= c + 1
    
