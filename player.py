from shoot import Shoot
class Player:
	def __init__(self,x = 0,y = 0, width = 99, height = 75, acceleration = 0, score = 0, life = 3, coins = 0,shield = False):
		self._x = x
		self._y = y
		self._width = width
		self._height = height
		self._imgSrc = "res/_player/player_1.png"
		self._shot = None
		self._acceleration = acceleration
		self._score = score
		self._life = life
		self._coins = coins
		self._shield = shield
	# METODOS GETTERS E SETTERS
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
	def getShot(self):
		return self._shot
	def setShot(self,shot):
		self._shot = shot
	def doShoot(self):
		self._shot = Shoot(self._x+self._height/2 + 5, self._y)
		self._shot.setAcceleration(15)
	def setX(self, x):
		self._x = x
	def setAcceleration(self,acc):
		self._acceleration = acc
	def getScore(self):
		return self._score 
	def setScore(self, score):
		self._score = score
	def getLife(self):
		return self._life
	def setLife(self, life):
		self._life = life
	def getCoins(self):
		return self._coins
	def setCoins(self,coins):
		self._coins = coins
	def getShield(self):
		return self._shield
	def setShield(self,shield):
		self._shield = shield
	def setImgSrc(self, imgSrc):
		self._imgSrc = imgSrc