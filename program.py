from graphics import *


def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint


def centrePoint(tlPoint, radius):
    x = tlPoint.getX() + radius
    y = tlPoint.getY() + radius
    centre = Point(x, y)
    return centre


def text(win, tlPoint, text, colour):
    p = centrePoint(tlPoint, 5)
    t = Text(p, text)
    t.setOutline(colour)
    t.draw(win)
    return t


def circlefromTL(win, tlPoint, radius, colour):
    centre = centrePoint(tlPoint, radius)
    circle(win, centre, radius, colour)


def circle(win, centre, radius, colour):
    c = Circle(centre, radius)
    c.setFill(colour)
    c.draw(win)
    return c


def rectangle(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    return r


def line(win, point1, point2, colour):
    l = Line(point1, point2)
    l.setOutline(colour)
    l.draw(win)
    return l


def patch2(win, colours, tlOffset):
    screenSize = 110
    scale = 20
    alternateFlag = True
    for y in range(0, screenSize, scale):
        for x in range(0, screenSize, scale):
            tl = Point(tlOffset.getX() + x, tlOffset.getY() + y)
            br = brPoint(tl, scale, scale)
            if alternateFlag:
                circlefromTL(win, tl, 10, colours[0])
            else:
                rectangle(win, tl, br, colours[2])

            alternateFlag = not alternateFlag


def patch1(win, colours, tlOffset):
    screenSize = 110
    scale = 20
    alternateFlag = True
    for y in range(0, screenSize, scale):
        for x in range(0, screenSize, scale):
            tl = Point(tlOffset.getX() + x, tlOffset.getY() + y)
            br = brPoint(tl, scale, scale)
            if alternateFlag:
                rectangle(win, tl, br, colours[1])
            else:
                circlefromTL(win, tl, 10, colours[3])
            alternateFlag = not alternateFlag


def main():
    screenSize = 500
    win = GraphWin("Test", screenSize, screenSize)
    colours = ["blue", "green", "orange", "white"]
    alternateFlag = True

    # STEP 1
    tlPoint = Point(0, 0)
    patch1(win, colours, tlPoint)
    # patch2(win, colours, tlPoint)

    # STEP 2
    # for i in range(4):
    #     tlPoint = win.getMouse()
    #     patch1(win, colours, tlPoint)
    #     tlPoint = win.getMouse()
    #     patch2(win, colours, tlPoint)

    # STEP 3
    # for y in range(0, screenSize, 100):
    #     for x in range(0, screenSize, 100):
    #         tlPoint = Point(x, y)
    #         if alternateFlag:  # if y  == 0 or x == 0   #or x == 400 or y == 400:
    #             patch2(win, colours, tlPoint)
    #         else:
    #             patch1(win, colours, tlPoint)
    #         alternateFlag = not alternateFlag
    win.getMouse()


main()
