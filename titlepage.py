from cmu_graphics import *
from PIL import Image
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5
def onAppStart(app):
    app.image = Image.open('titlefrog.PNG')
    app.image = CMUImage(app.image)
    app.playbutton = Image.open('playbutton.PNG')
    app.playbutton = CMUImage(app.playbutton)
    app.frogbutton = Image.open('frogbutton.PNG')
    app.frogbutton = CMUImage(app.frogbutton)
    app.titlecard = True
    app.angle = 0
def redrawAll(app):
    if app.titlecard == True:
        drawImage(app.image,app.width/2,app.height/2, align='center')
        drawCircle(1200 *2/3,450,165, fill = 'cornSilk' )
        drawCircle(1200 *2/3,450,150, fill = 'violet' )
        drawImage(app.frogbutton,535,165,rotateAngle=app.angle)

def onMousePress(app, mouseX, mouseY):
    cx = app.width *2/3
    cy = app.height/2
    r =app.width/5
    if distance(cx,cy,mouseX,mouseY) <= r:
        app.titlecard = False
def onStep(app):
    app.angle += 5
def main():
    runApp(1200,800)

if __name__ == '__main__':
    main()  