class Meteoro(object):
    def __init__(self,x = 0,y = 0, width = 43, height = 43, acceleration = 4, imgSrc = ""):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._acceleration = acceleration
        self._imgSrc = imgSrc
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getImgSrc(self):
        return self._imgSrc
    def getAcceleration(self):
        return self._acceleration
    def setAccelaration(self, acceleration):
        self._acceleration = acceleration
    def setX(self,x):
        self._x = x
    def setY(self,y):
        self._y = y
    def setHeight(self, height):
        self._height = height
    def setImgSrc(self,imgSrc):
        self._imgSrc = imgSrc
