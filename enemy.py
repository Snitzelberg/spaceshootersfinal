from shoot import Shoot
class Enemy:
	def __init__(self, x = 0, y = 0, width = 71, height = 64, imgSrc = "res/_enemies/enemy_1.png", acceleration = 0, shot = None):
		self._x = x
		self._y = y 
		self._width = width
		self._height = height
		self._imgSrc = imgSrc
		self._accelaration = acceleration
		self._shot = shot
	# GETTERS E SETTERS
	def setX(self,x):
		self._x = x
	def setY(self,y):
		self._y = y
	def getWidth(self):
		return self._width
	def getHeight(self):
		return self._height
	def getX(self):
		return self._x
	def getY(self):
		return self._y
	def getShot(self):
		return self._shot
	def setShot(self, shot):
		self._shot = shot
	def doShoot(self):
		self._shot = Shoot(self._x+self._height/2 + 5, self._y)
		self._shot.setAcceleration(15)
