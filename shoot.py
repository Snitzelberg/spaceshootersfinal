class Shoot:
	def __init__(self, x = 0, y = 0, width=9, height=57, acceleration = 0):
		self._x = x
		self._y = y
		self._width = width
		self._height = height
		self._imgSrc = "res/_player/laser_shoot.png"
		self._acceleration = acceleration
	def getX(self):
		return self._x
	def getY(self):
		return self._y
	def setY(self,y):
		self._y = y
	def getWidth(self):
		return self._width
	def getHeight(self):
		return self._height
	def getImg(self):
		return self._imgSrc
	def getAcceleration(self):
		return self._acceleration
	def setAcceleration(self, acc):
		self._acceleration = acc
