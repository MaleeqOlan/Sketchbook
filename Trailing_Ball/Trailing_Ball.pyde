def setup():
    size(1000,1000)
    colorMode(HSB)
    x = 0
    y = 0
    c = 0
    background(0)
    
    
xdir = 1
ydir = 1


def draw():
    global x
    global y
    global c
    
    global xdir
    global ydir
    
    blendMode(SUBTRACT)
    colorMode(RGB)
    fill(255,10)
    rect(0,0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
        
    noStroke()   
    fill(c, 255, 255)  
    circle(x,y,200)
    x = x + xdir
    y = y + ydir
    c = c + 1
    
    if c > 255:
        c = 0
        
    if x > width:
        xdir = xdir
    
    
