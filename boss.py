from shoot import Shoot
class Boss:
    __contadorTiros = 0
    __tiros = []
    def __init__(self, x = 0,y = 0, width=239,height=182,img = "",velocidade = 1, life = 1):
        self.__x = x
        self.__y = y 
        self.__width = width
        self.__height = height
        self.__img = img
        self.__velocidade = velocidade
        self.__life = life
    def getImg(self):
        return self.__img
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setX(self,x):
        self.__x = x
    def setVelocidade(self,velocidade):
        self.__velocidade = velocidade
    def getVelocidade(self):
        return self.__velocidade
    def getLife(self):
        return self.__life
    def setLife(self,life):
        self.__life = life
    def getContadorTiros(self):
        return self.__contadorTiros
    def setContadorTiros(self, tiros):
        self.__contadorTiros = tiros
    def getTiros(self):
        return self.__tiros
    def setTiros(self,tiros):
        self.__tiros = tiros
