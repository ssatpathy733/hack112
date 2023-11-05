from cmu_graphics import *
from PIL import Image
import random

def onAppStart(app):
    app.allTasks = [["shower", "brush your teeth", "bubbly bath", "skincare"],
                    ["get booba", "drink wotta", "make le pizza", "make hot choccy!!"], 
                    ["sing", "play games", "talk to your friends (not about school >:()", "watch a show"]]
    app.currTasks = []
    getCurrTasks(app)
    app.width = 1200
    app.height = 800
    app.row = 3
    app.col = 4
    app.stickerbook = stickerbookSetup(app.row, app.col)

    app.infoButton = 100, 100, 100, 100     # coords x, y, then dimensions
    app.infoBoxDimensions = 600, 300        # dimensions x, y


    app.stickerButton = 300, 100, 100, 100  # coords x, y, then dimensions
    app.stickerBoxDimensions = 800, 500     # dimensions x, y
    app.stickerBoxMargins = 10
    app.stickerBoxHide = (app.stickerBoxDimensions[0] - (app.stickerBoxMargins*5))//app.col, (app.stickerBoxDimensions[1] - (app.stickerBoxMargins*4))//app.row           # dimensions x, y

    app.showInfo = False
    app.showStickers = False

    app.instructions = '''
    Complete tasks to unlock sticker packs.
    Something more.
    Instructions,, yay
    I dont know this is just filler :3
    '''

    app.instructionsSplit =  app.instructions.splitlines()
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

def drawStickerBoxes(app, top, left):
    for i in range(len(app.stickerbook)):
        for j in range(len(app.stickerbook[i])):
            if app.stickerbook[i][j] == False: # if sticker is already found
                drawRect(app.stickerBoxMargins + left + (app.stickerBoxHide[0] + 10) * j, app.stickerBoxMargins + top + (app.stickerBoxHide[1] + 10) * i, app.stickerBoxHide[0], app.stickerBoxHide[1], fill = "pink")

def showInfo(app):
    drawRect(app.width//2, app.height//2, app.infoBoxDimensions[0], app.infoBoxDimensions[1], align = 'center', fill = "pink")
    for i in range(len(app.instructionsSplit)):
        drawLabel(app.instructionsSplit[i], app.width//2 - 200, (app.height//2 - 100) + i * 20, align= "left")
    

def showStickers(app):
    drawRect(app.width//2, app.height//2, app.stickerBoxDimensions[0], app.stickerBoxDimensions[1], align = 'center', fill = "purple")
    # drawImage(app.url, app.width//2, app.height//2, align = "center")
    drawStickerBoxes(app, app.height//2 - app.stickerBoxDimensions[1]//2, app.width//2 - app.stickerBoxDimensions[0]//2)

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

def temp_buttons(app):
    drawRect(app.infoButton[0], app.infoButton[1], 100, 100, fill = "red")
    drawRect(app.stickerButton[0], app.stickerButton[1], 100, 100, fill = "blue")

def onMousePress(app, mouseX, mouseY):
    cx = app.width *2/3
    cy = app.height/2
    r =app.width/5
    if distance(cx,cy,mouseX,mouseY) <= r:
        app.titlecard = False
    if mouseX > app.infoButton[0] and mouseX < app.infoButton[0]+app.infoButton[2] and mouseY > app.infoButton[1] and mouseY < app.infoButton[1]+app.infoButton[3]:
        app.showInfo = not app.showInfo
    if mouseX > app.stickerButton[0] and mouseX < app.stickerButton[0]+app.stickerButton[2] and mouseY > app.stickerButton[1] and mouseY < app.stickerButton[1]+app.stickerButton[3]:
        app.showStickers = not app.showStickers


def onStep(app):
    app.angle += 5

def redrawAll(app):
    drawChecklist(app)
    # if app.titlecard == True:
        # drawImage(app.image,app.width/2,app.height/2, align='center')
        # drawCircle(1200 *2/3,450,165, fill = 'cornSilk' )
        # drawCircle(1200 *2/3,450,150, fill = 'violet' )
        # drawImage(app.frogbutton,535,165,rotateAngle=app.angle)
    temp_buttons(app)

    if app.showInfo:
        showInfo(app)
    if app.showStickers:
        showStickers(app)

def main():
    runApp(1200, 800)
    
main()