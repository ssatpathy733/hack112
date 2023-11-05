from cmu_graphics import *
from PIL import Image
import random

def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.row = 3
    app.col = 4
    app.stickerbook = stickerbookSetup(app.row, app.col)
    app.url = "cmu://664537/26105090/frog_stickers.jpg"
    app.allTasks = [["shower", "brush your teeth", "bubbly bath", "skincare"],
                    ["get booba", "drink wotta", "make le pizza", "make hot choccy!!"], 
                    ["sing", "play games", "talk to your friends (not about school >:()", "watch a show"]]
    app.currTasks = []
    getCurrTasks(app)
    app.infoButton = 10, 10
    app.stickerButton = 30, 10
    app.checkBoxesTopLeft = (20, 660)
    app.image = Image.open('titlefrog.PNG')
    app.image = CMUImage(app.image)
    app.playbutton = Image.open('playbutton.PNG')
    app.playbutton = CMUImage(app.playbutton)
    app.frogbutton = Image.open('frogbutton.PNG')
    app.frogbutton = CMUImage(app.frogbutton)
    app.titlecard = True
    app.angle = 0
    
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def getCurrTasks(app):
    for row in range(len(app.allTasks)):
        currNum = random.randrange(0, len(app.allTasks[row]))
        (app.currTasks).append((row, currNum))

def stickerbookSetup(rows, cols):
    stickers = [[False]*cols for i in range(rows)]
    return stickers

def revealSticker(app, taskTuple):
    app.stickers[taskTuple[0]][taskTuple[1]] == True
    return(f"Sticker at {taskTuple[0]}, {taskTuple[1]} is now True" )

def drawStickerBoxes(app):
    for i in range(len(app.stickerbook)):
        for j in range(len(app.stickerbook[i])):
            if app.stickerbook[i][j]: # if sticker is already found
                drawRect(x*25, y*25, x+20, y+20, fill = "pink")

def drawChecklist(app):
    left, top = app.checkBoxesTopLeft 
    drawRect(0, 600, app.width, 200, fill=rgb(214, 132, 154))
    drawLine(0, 600, app.width, 600, fill="black")
    drawLabel("Today's Tasks! :0", left, 630, size=40, align="left", font = "montserrat", fill="white")
    for i in range(len(app.currTasks)):
        row, col = app.currTasks[i]
        top += 10
        drawRect(left, top, 30, 30, border = "white", fill=rgb(214, 132, 154))
        drawLabel(f"{app.allTasks[row][col]}", left + 60, top + 15, align = "left", size = 30, fill="white", font = "montserrat")
        top += 30

def onMousePress(app, mouseX, mouseY):
    cx = app.width *2/3
    cy = app.height/2
    r =app.width/5
    if distance(cx,cy,mouseX,mouseY) <= r:
        app.titlecard = False
def onStep(app):
    app.angle += 5

def redrawAll(app):
    drawChecklist(app)
    if app.titlecard == True:
        drawImage(app.image,app.width/2,app.height/2, align='center')
        drawCircle(1200 *2/3,450,165, fill = 'cornSilk' )
        drawCircle(1200 *2/3,450,150, fill = 'violet' )
        drawImage(app.frogbutton,535,165,rotateAngle=app.angle)

def main():
    runApp(1200, 800)
    
main()