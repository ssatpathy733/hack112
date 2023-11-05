from cmu_graphics import *
from PIL import Image
import random

def onAppStart(app):
    app.allTasks = [["shower", "brush your teeth", "bubbly bath", "skincare"],
                    ["get booba", "drink wotta", "make le pizza", "make hot choccy!!"], 
                    ["sing", "play games", "talk to your friends (not about school >:()", "watch a show"]]
    app.currTasks = []
    getCurrTasks(app)
    app.checkListColors = ["white", "white", "white"]
    app.width = 1200
    app.height = 800
    app.row = 3
    app.col = 4
    app.newDay = False
    app.stickerbook = stickerbookSetup(app.row, app.col)

    app.infoButton = 25, 25, 50, 50     # coords x, y, then dimensions
    app.infoBoxDimensions = 600, 300        # dimensions x, y


    app.stickerButton = 1025, 25, 150, 50  # coords x, y, then dimensions
    app.stickerBoxDimensions = 800, 500     # dimensions x, y
    app.stickerBoxMargins = 10
    app.stickerBoxHide = (app.stickerBoxDimensions[0] - (app.stickerBoxMargins*5))//app.col, (app.stickerBoxDimensions[1] - (app.stickerBoxMargins*4))//app.row           # dimensions x, y

    app.showInfo = False
    app.showStickers = False

    app.instructions = '''
    How to play "A Hoppy Day": A Mental Health Game With Original Art
    Begin by pressing the spinning frog. You will be presented with 3 self 
    care tasks that you have one day to complete. Complete as many as you 
    can to have a hoppier day :)

    A Hoppy Day!" is a game/self-help app that aims to gently remind the 
    player to take care of themselves throughout the day. Each day, the 
    player is provided with small tasks to complete such as taking a shower, 
    drinking water,  or talking to friends. The goal of this game is for the 
    player to take a step away from their work, relieve some stress, and 
    enjoy spending time with digital frogs. This is extremely pertinent to 
    students at CMU as the university is known for its heavy workload and 
    long hours. 
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

    app.beforeskincare = Image.open('beforeskincare.PNG')
    app.beforeskincare = CMUImage(app.beforeskincare)
    app.afterskincare = Image.open('afterskincare.PNG')
    app.afterskincare = CMUImage(app.afterskincare)
    app.brushteeth = Image.open('brushteeth.PNG')
    app.brushteeth = CMUImage(app.brushteeth)
    app.shower = Image.open('shower.PNG')
    app.shower = CMUImage(app.shower)
    app.toothbrush = Image.open('toothbrush.PNG')
    app.toothbrush = CMUImage(app.toothbrush)
    app.soapbar = Image.open('soapbar.PNG')
    app.soapbar = CMUImage(app.soapbar)
    app.timecountbrush = 0
    app.timecountshower = 0
    app.brushing = False
    app.showering = False
    app.skin = True
    app.brushcx = 200
    app.brushcy = 200
    app.soapcx = 200
    app.soapcy = 200
    app.whiskcx = 200
    app.whiskcy = 200
    app.cooking = False
    app.timecountcooking = 0
    app.frog_bg = Image.open('food_bg.PNG')
    app.frog_bg = CMUImage(app.frog_bg)
    app.frog_whisk = Image.open('food_whisk.PNG')
    app.frog_whisk = CMUImage(app.frog_whisk)

    app.box1, app.box2, app.box3 = False, False, False

    app.mainbackground = Image.open('backgroundmain.PNG')
    app.mainbackground = CMUImage(app.mainbackground)

    app.currAnimation = None
    app.currAnimation2 = None

    app.stickers = Image.open('stickerfrog.png')
    app.stickers = CMUImage(app.stickers)
    
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def onStep(app):
    if app.titlecard:
        app.angle += 5
    elif app.brushing == True:
        app.timecountbrush+=1
    elif app.showering == True:
        app.timecountshower+=1
    elif app.cooking == True:
        app.timecountcooking+=1
    # newDay(app)

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
    # for i in range(len(app.stickerbook)):
    #     for j in range(len(app.stickerbook[i])):
    #         if app.stickerbook[i][j] == False: # if sticker is already found
    #             drawRect(app.stickerBoxMargins + left + (app.stickerBoxHide[0] + 10) * j, app.stickerBoxMargins + top + (app.stickerBoxHide[1] + 10) * i, app.stickerBoxHide[0], app.stickerBoxHide[1], fill = "pink")
    drawImage(app.stickers,600,400,align = 'center')

def showInfo(app):
    drawRect(app.width//2, app.height//2, app.infoBoxDimensions[0], app.infoBoxDimensions[1], align = 'center', fill = "pink")
    for i in range(len(app.instructionsSplit)):
        drawLabel(app.instructionsSplit[i], app.width//2 - 200, (app.height//2 - 100) + i * 20 - 40, align= "left", fill="white")
    

def showStickers(app):
    # drawRect(app.width//2, app.height//2, app.stickerBoxDimensions[0], app.stickerBoxDimensions[1], align = 'center', fill = "purple")
    #  drawImage(app.url, app.width//2, app.height//2, align = "center")
    drawStickerBoxes(app, app.height//2 - app.stickerBoxDimensions[1]//2, app.width//2 - app.stickerBoxDimensions[0]//2)

def drawChecklist(app):
    left, top = app.checkBoxesTopLeft 
    drawRect(0, 600, app.width, 200, fill= "pink")
    drawLine(0, 600, app.width, 600, fill=rgb(214, 132, 154))
    drawLabel("Today's Tasks! :0", left, 630, size=40, align="left", font = "montserrat", fill=rgb(214, 132, 154))
    for i in range(len(app.currTasks)):
        row, col = app.currTasks[i]
        top += 10
        drawRect(left, top, 30, 30, border = app.checkListColors[i], fill="pink")
        drawLabel(f"{app.allTasks[row][col]}", left + 60, top + 15, align = "left", size = 30, fill= app.checkListColors[i], font = "montserrat")
        top += 30

def temp_buttons(app):
    drawRect(app.infoButton[0], app.infoButton[1], app.infoButton[2], app.infoButton[3], fill = "pink", border=rgb(214, 132, 154))
    drawLabel("i", app.infoButton[0] + app.infoButton[2]//2, app.infoButton[1] + app.infoButton[3]//2, fill="white", bold = True, size = 24)
    drawRect(app.stickerButton[0], app.stickerButton[1], app.stickerButton[2], app.stickerButton[3], fill = "pink", border=rgb(214, 132, 154))
    drawLabel("Stickers", app.stickerButton[0] + app.stickerButton[2]//2, app.stickerButton[1] + app.stickerButton[3]//2, fill = "white", bold = True, size = 24)

def onMouseMove(app,mouseX,mouseY):
    if app.brushing == True:
        app.brushcx = mouseX
        app.brushcy = mouseY
    elif app.showering == True:
        app.soapcx = mouseX
        app.soapcy = mouseY
    elif app.cooking == True:
        app.whiskcx = mouseX
        app.whiskcy = mouseY

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
    if app.skin == False:
        cx = 800
        cy = 200
        r = 40 
        if distance(cx,cy,mouseX,mouseY) <= r:
            app.skin = True
    if mouseX >= 20 and mouseX <= 50: 
        if mouseY >= 660 and mouseY <= 690:
            app.checkListColors[0] = "green"
            app.box1 = True
            row, col = app.currTasks[0]
            app.currAnimation = app.allTasks[row][col]
            row2, col2 = app.currTasks[1]
            app.currAnimation2 = app.allTasks[row2][col2]
            print(app.currAnimation)
            if app.currAnimation == "brush your teeth":
                app.brushing = True
            if app.currAnimation == "skincare":
                app.skin = False
            elif app.currAnimation == "shower" or "bubbly bath":
                app.showering = True
            if app.timecountbrush > 150:
                app.timecountbrush = 0
                app.brushing = False
            if app.timecountshower > 150:
                app.timecountshower = 0
                app.showering = False
        if mouseY >= 710 and mouseY <= 740:
            app.checkListColors[1] = "green"
            app.box2 = True
            app.currAnimation = app.currTasks[1]
            if app.currAnimation2 == "get booba" or "drink wotta" or "make le pizza" or "make hot choccy!!":
                app.cooking = True
        if mouseY >= 760 and mouseY <= 790:
            app.checkListColors[2] = "green"
            app.box3 = True
            app.currAnimation = app.currTasks[2]
        if app.box1 == app.box2 == app.box3 == True and mouseX >= 1100 and mouseX <= 1250 and mouseY >= 750 and mouseY <= 800:
            app.newDay = True
            app.box1, app.box2, app.box3 = False, False, False
    print(mouseX, mouseY)

def brushteeth(app):
    brushing = True
    if brushing == True and app.timecountbrush < 150:
        drawImage(app.brushteeth,app.width/2,app.height/2, align='center')
        drawImage(app.toothbrush,app.brushcx,app.brushcy, align='center')
    else:
        brushing = False

def shower(app):
    showering = True
    if showering == True and app.timecountshower < 150:
        drawImage(app.shower,app.width/2,app.height/2, align='center')
        drawImage(app.soapbar,app.soapcx,app.soapcy, align='center')
    else:
        showering = False

def skincare(app):
    if app.skin == False:
        drawImage(app.afterskincare,app.width/2,app.height/2, align='center')
        drawCircle(800,200,40, fill = 'violet')
        drawLabel('Go Back',800,200,size = 20, fill = 'white')
    if app.skin == True:
        drawImage(app.afterskincare,app.width/2,app.height/2, align='center')
        drawCircle(800,200,40, fill = 'violet')

def cooking(app):
    cooking = True
    if cooking == True and app.timecountcooking < 150:
        drawImage(app.frog_bg,app.width/2,app.height/2, align='center')
        drawImage(app.frog_whisk,app.whiskcx,app.whiskcy, align='center')
    else:
        cooking = False

def newDay(app):
    if app.newDay == True:
        app.currTasks = []
        getCurrTasks(app)
        app.checkListColors[0], app.checkListColors[1], app.checkListColors[2] = "white", "white", "white"
        app.newDay = False


def redrawAll(app):
    drawImage(app.mainbackground,app.width/2,app.height/2, align="center")
    drawChecklist(app)
    temp_buttons(app)
    drawRect(1100, 750, 150, 50, align="center", fill = "purple", border=rgb(214, 132, 154))
    drawLabel("New Day!", 1100, 750, align="center", fill = "white", bold = True, size = 24)
    if app.titlecard == True:
        drawImage(app.image,app.width/2,app.height/2, align='center')
        drawCircle(1200 *2/3,450,165, fill = 'cornSilk' )
        drawCircle(1200 *2/3,450,150, fill = 'violet' )
        drawImage(app.frogbutton,535,165,rotateAngle=app.angle)
    if app.box1 == True:
            drawLine(20, 670, 50, 700, fill = "green")
            drawLine(50, 670, 20, 700, fill = "green")
            if app.brushing == True:
                brushteeth(app)
            if app.showering == True:
                shower(app)
            if app.skin == False:
                skincare(app)
    if app.box2 == True:
            drawLine(20, 710, 50, 740, fill = "green")
            drawLine(50, 710, 20, 740, fill = "green")
            if app.cooking == True:
                cooking(app)
    if app.box3 == True:
            drawLine(20, 750, 50, 780, fill = "green")
            drawLine(50, 750, 20, 780, fill = "green")
    if app.showInfo:
        showInfo(app)
    if app.showStickers:
        showStickers(app)
    
    

def main():
    runApp(1200, 800)
    
main()