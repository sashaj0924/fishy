def setup():
    size(400, 400)
    background (0, 102, 255)
    x = 0
    
    
    while x < 400:
        y = 0
        while y < 400:
            if x % 200 == 0:
                fish(150, 150)
                fish(200, 200)
            else:
                    fish(50,100)
                    fish(50, 300)
            if y % 300 == 0:
                    fish(150, 150)
            y = y + 100
            x = x + 100
    
def fish(xCoordinate, yCoordinate):
    fill(random(253), random(253), random(253))
    ellipse(xCoordinate, yCoordinate, 100, 50)
    triangle(xCoordinate+45, yCoordinate, xCoordinate+100, yCoordinate+30,xCoordinate+100,yCoordinate-50)
    
