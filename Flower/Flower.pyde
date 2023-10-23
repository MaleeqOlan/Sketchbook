def setup():
    size(800, 800)
    flower(400, 400, 120, 8)
    sunflower(400, 400)
   
def sunflower(x, y):
    stroke(0)
    fill(150,60,0)
    for i in range(200):
        angle = i * radians(137.5)  # Golden angle (137.5 degrees in radians)
        radius = 6.5 * sqrt(i)  # Increase the radius proportionally
        x_pos = x + radius * cos(angle)
        y_pos = y + radius * sin(angle)
        ellipse(x_pos, y_pos, 10, 10)

def flower(x, y, radius, petal_count):
    strokeWeight(5)
    stroke(0,0,0)
    fill(200,20,200)
   
    angle_offset = TWO_PI / petal_count
   
    for i in range(petal_count):
        angle = i * angle_offset
        x_petal = x + radius * cos(angle)
        y_petal = y + radius * sin(angle)
       
        
        petal_length = 250
        petal_width = 160
       
        pushMatrix()
        translate(x_petal, y_petal)
        rotate(angle + PI/2)  # Rotate by 90 degrees
        ellipse(0, 0, petal_width, petal_length)
        popMatrix()
