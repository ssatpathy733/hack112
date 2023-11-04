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
    app.infoButton = 10, 10
    app.stickerButton = 30, 10
    getCurrTasks(app)
    
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

def main():
    runApp()
    
main()