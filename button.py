# button.py
# Button class

from graphics import*

class Button:

    """This class creates a rectangular button which is initially inactive"""
    def __init__(self, win, center, width, height, label, color='yellow'):
        w, h = width / 2.0, height / 2.0
        x, y = center. getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    "A function to click the button"
    def clicked(self,p):
        if self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax:
            return 1

    "A function to get the label of the button"
    def getLabel(self):
        return self.label.getText()

    "This function sets this button to 'active'"
    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    "This function sets this button to 'inactive'"
    def deactivate(self):
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0


