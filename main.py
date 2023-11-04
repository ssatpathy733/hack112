from cmu_graphics import *
import random

def onAppStart(app):
    app.allTasks = [["shower", "brush your teeth", "bubbly bath", "skincare"],
                    ["get booba", "drink wotta", "make le pizza", "make hot choccy!!"], 
                    ["sing", "play games", "talk to your friends (not about school >:()", "watch a show"]]
    app.currTasks = []
    getCurrTasks(app)
    
def getCurrTasks(app):
    for row in range(len(app.allTasks)):
        currNum = random.randrange(0, len(app.allTasks[row]))
        (app.currTasks).append((row, currNum))

def main():
    runApp()
    
main()