def setup():
    size(500,500)
    
    
def draw():
    background(300,400,0)
    noStroke()
    fill(300,0,100)
    
#<less >greater
# == the same
#<= less than or equal to
#>= greater than or equal to
# and 
# or

    if mouseX < width / 2 and mouseY < height / 2:
        rect(0, 0,width / 2, height/2)
    elif mouseX > width/2 and mouseY < height/2:
        rect(width / 2,0, width/ 2, height / 2)
    elif mouseX > width/2 and mouseY < height/2:
        rect(width / 2,0, width/ 2, height / 2)
    else:
        rect(width / 2,height / 2,width / 2,height / 2)
