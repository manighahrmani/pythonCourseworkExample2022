from graphics import *


def drawSmileyFace(win, topLeftX, topLeftY, eyeColour, mouthColour):
    face = Circle(Point(topLeftX + 30, topLeftY + 30), 30)
    face.setFill("white")
    face.draw(win)

    mouthCircle = Circle(Point(topLeftX + 30, topLeftY + 40), 15)
    mouthCircle.setFill(mouthColour)
    mouthCircle.draw(win)

    # draw a white rectangle covering upper half of mouth
    mouthCover = Rectangle(Point(topLeftX + 10, topLeftY + 10),
                           Point(topLeftX + 50, topLeftY + 40))
    mouthCover.setFill("white")
    mouthCover.setWidth(0)
    mouthCover.draw(win)

    leftEye = Circle(Point(topLeftX + 20, topLeftY + 20), 5)
    rightEye = Circle(Point(topLeftX + 40, topLeftY + 20), 5)
    leftEye.setFill(eyeColour)
    rightEye.setFill(eyeColour)
    leftEye.draw(win)
    rightEye.draw(win)


def main():
    win = GraphWin("Smiley Face", 200, 200)
    drawSmileyFace(win, 0, 0, "blue", "red")
    win.getMouse()


main()
