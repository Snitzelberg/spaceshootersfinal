# -*- coding: utf-8 -*-
import sys, pygame, os
import random
from player import Player
from enemy import Enemy
from meteoro import Meteoro
from boss import Boss
from shoot import Shoot
from game_db import *
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
size = width, height = 1000, 700
vetImagens = []
numLinhas = 0
numCol = 0
bossFinal = Boss(width/2-120,60,239,182,pygame.image.load("res/_enemies/boss_1.png"))
vetEnemies = [None]*numLinhas
for x in range(0,numLinhas):
	vetEnemies[x] = [None]*numCol
for a in range(0,numLinhas):
	for b in range(0,numCol):
		e = Enemy()
		e.setX(50+(e.getWidth()*b)+15*b)
		e.setY(20+(e.getHeight()*a)+15*a)
		vetEnemies[a][b] = e
for y in range(0,10):
	vetImagens.append(pygame.image.load("res/_ui/numeral"+str(y)+".png"))
player = Player((width/2)-(99/2),(height-75)-20)
playerImg = pygame.image.load(player.getImgSrc())
shootImg = pygame.image.load("res/_lasers/laser_shoot.png")
shootImgEnemy = pygame.image.load("res/_lasers/laser_shoot_red.png")
enemyImg = pygame.image.load("res/_enemies/enemy_1.png")
greyPanel = pygame.image.load("res/_ui/grey_panel.png")
back = pygame.image.load("res/_ui/Backward_BTN.png")
# Vida Jogador
playerLifeImg = pygame.image.load("res/_ui/playerLife1_blue.png")
xLifeImg = pygame.image.load("res/_ui/numeralX.png")
vetNums = [pygame.image.load("res/_ui/numeral1.png"),pygame.image.load("res/_ui/numeral2.png"),pygame.image.load("res/_ui/numeral3.png"),pygame.image.load("res/_ui/numeral4.png")]
# Meteoro Imgs
vetMeteoros = [pygame.image.load("res/_meteors/meteor_brown_1.png"),pygame.image.load("res/_meteors/meteor_grey_1.png")]
vetObjMeteoros = []
# Loja 
def gameShop():
	gameShop = True
	def comprarItem(preco,img):
		if player.getCoins() - preco >= 0:
			player.setCoins(player.getCoins()-preco)
			if img != "res/_power/Heart_symbol.png":
				player.setImgSrc(img)
				save_score(player)
			else:
				player.setLife(4)
				save_life(player)
			pygame.mixer.music.load("sounds/lojinha.ogg")
			pygame.mixer.music.play()
			# Volta p/ menu principal
			gameMenu()
	myFont = pygame.font.Font("sounds/kenvector_future.ttf", 20)
	# Fontes do Painel de Compra
	text = myFont.render("Moedas: "+str(player.getCoins()), True, (255, 255, 255))
	text2 = myFont.render("Skins(20 Moedas): ", True, (255, 255, 255))
	imgLoad = ""
	posX, posY = 0,80
	# Atual
	if player.getImgSrc() == "res/_player/player_1.png":
		imgLoad = pygame.image.load("res/_ui/blue_sliderDown.png")
		posX = 305
	elif player.getImgSrc() == "res/_player/player_2.png":
		imgLoad = pygame.image.load("res/_ui/red_sliderDown.png")
		posX = 60
	elif player.getImgSrc() == "res/_player/player_3.png":
		imgLoad = pygame.image.load("res/_ui/green_sliderDown.png")
		posX = 178
	elif player.getImgSrc() == "res/_player/Ovni.png":
		imgLoad = pygame.image.load("res/_ui/blue_sliderDown.png")
		posX = 425

	# Skins disponiveis
	player_blue = pygame.image.load("res/_player/player_1.png")
	player_orange = pygame.image.load("res/_player/player_2.png")
	player_green = pygame.image.load("res/_player/player_3.png")
	ovni = pygame.image.load("res/_player/Ovni.png")
	life = pygame.image.load("res/_power/Heart_symbol.png")

	# Logica do Shop
	while gameShop:
		# Fundo 
		gameDisplay.fill((0,0,0))
		gameDisplay.blit(bgImage,(0,0))
		gameDisplay.blit(text,(10,10))
		gameDisplay.blit(text2,(10,40))
		# Comprar Skins
		gameDisplay.blit(greyPanel,(50,80))
		gameDisplay.blit(greyPanel,(170,80))
		gameDisplay.blit(greyPanel,(295,80))
		gameDisplay.blit(greyPanel, (420, 80))
		gameDisplay.blit(player_orange,(58,100))
		gameDisplay.blit(player_green,(178,100))
		gameDisplay.blit(player_blue,(305,100))
		gameDisplay.blit(ovni, (435, 105))
		gameDisplay.blit(imgLoad,(posX,posY))
		# Painel para Comprar vida
		if player.getLife() <= 3:
			gameDisplay.blit(greyPanel,(50,220))
			gameDisplay.blit(life,(63,235))
		# Exit icon
		gameDisplay.blit(back,(width-110,height-110))
		# Eventos 
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # FECHAR O GAME
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				x,y = pygame.mouse.get_pos()
				pygame.mixer.music.load("sounds/click1.ogg")
				pygame.mixer.music.play()
				if x >= 915 and x <= 965 and y >= 610 and y <= 675:
					gameShop = False
					gameMenu()
					break
				if x >= 50 and x <= 167 and y >= 95 and y <= 203:
					posX = 60
					comprarItem(20,"res/_player/player_2.png")
				elif x >= 185 and x <= 286 and y >= 95 and y <= 203:
					posX = 178
					comprarItem(20,"res/_player/player_3.png")
				elif x >= 308 and x <= 414 and y >= 95 and y <= 203:
					posX = 305
					comprarItem(20,"res/_player/player_1.png")
				elif x >= 423 and x <= 527 and y >= 95 and y <= 203:
					posX = 420
					comprarItem(200,"res/_player/Ovni.png")
				elif x >= 50 and x <= 167 and y >= 220 and y <= 338 and player.getLife() <= 3:
					comprarItem(50,"res/_power/Heart_symbol.png")
		# Desenhando Cursor
		x,y = pygame.mouse.get_pos()
		gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
		# Update
		pygame.display.update()
		clock.tick(20)
# Metodos Principais
hpTable = pygame.image.load("res/_ui/Boss_HP_Table.png")
hpBar = pygame.image.load("res/_ui/Boss_HP_Bar_2.png")
def draw():
	# Fundo
	gameDisplay.fill((0,0,0))
	gameDisplay.blit(bgImage,(0,0))
	# Escrevendo vida
	gameDisplay.blit(playerLifeImg,(10,(height-30)))
	gameDisplay.blit(xLifeImg,(45,(height-25)))
	numeralImg = vetNums[player.getLife()-1]
	gameDisplay.blit(numeralImg,(65,(height-25)))
	# Escrevendo pontução
	size = len(str(player.getScore()))
	xInit = width - 20 - (20*size)
	contador = 0
	for x in str(player.getScore()):
		gameDisplay.blit(vetImagens[int(x)],(xInit+(contador*20),15))
		contador += 1
	# Player Img 
	playerImg = pygame.image.load(player.getImgSrc())
	gameDisplay.blit(playerImg,(player._x,player._y))
	# Desenhando
	t = 0
	for v in vetEnemies:
		t += v.count(None)	
	if t == numCol * numLinhas:
		if bossFinal.getLife() > 0:
			gameDisplay.blit(bossFinal.getImg(),(bossFinal.getX(),bossFinal.getY()))
			gameDisplay.blit(hpTable,(30,15))
			sub = hpBar.subsurface(0, 0, 750*bossFinal.getLife(), 14)
			gameDisplay.blit(sub,(45,20))
			for myVar in bossFinal.getTiros():
				gameDisplay.blit(shootImgEnemy,(myVar.getX(),myVar.getY()))
	else:
		for x in vetEnemies:
			for y in x:
				if y != None:
					if y.getShot() != None:
						gameDisplay.blit(shootImgEnemy,(y.getShot().getX(),y.getShot().getY()))
					gameDisplay.blit(enemyImg,(y.getX(), y.getY()))
	# Tiro 
	if player.getShot() != None:
		gameDisplay.blit(shootImg,(player.getShot().getX(), player.getShot().getY()))
	# Meteoro
	for meteoro in vetObjMeteoros:
		gameDisplay.blit(meteoro.getImgSrc(),(meteoro.getX(),meteoro.getY()))
	# Desenhando Cursor
	x,y = pygame.mouse.get_pos()
	gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
# Game Win
def gameWin():
	# Game On
	gameOn = False
	while not gameOn:
		# Fundo
		gameDisplay.fill((0,0,0))
		gameDisplay.blit(bgImage, (0, 0))
		# Texto
		x,y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Fechar o Game
				save_score(player)
				sys.exit()
		# Desenhando
		gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
		myFont = pygame.font.Font("sounds/kenvector_future.ttf", 150)
		myFont2 = pygame.font.Font("sounds/kenvector_future.ttf", 20)
		text = myFont.render("You Win!", True, (0, 255, 0))
		text2 = myFont2.render("Parabéns !!",True,(255, 255, 255))
		text3 = myFont2.render("Caso queira jogar novamente, recarregue o jogo",True, (255, 255, 255))
		gameDisplay.blit(text,(100, 200))
		gameDisplay.blit(text2,(150,400))
		gameDisplay.blit(text3,(150,450))
		size = len(str(player.getScore()))
		contador = 0
		for x in str(player.getScore()):
			gameDisplay.blit(vetImagens[int(x)], (150 + (contador * 20), 500))
			contador += 1
		# Update 
		pygame.display.update()
		clock.tick(15)
# Game Over
def gameOver():
	# Game On
	gameOn = False
	myFont = pygame.font.Font("sounds/kenvector_future.ttf", 100)
	myFont2 = pygame.font.Font("sounds/kenvector_future.ttf", 20)
	text = myFont.render("Game Over", True, (255, 0, 0))
	text2 = myFont2.render("Você possui " + str(player.getCoins()) + " moedas.", True, (255, 255, 255))

	while not gameOn:
		# Fundo
		gameDisplay.fill((0,0,0))
		gameDisplay.blit(bgImage,(0,0))
		widthT1, heightT1 = myFont.size("Space Shooters")
		# Texto
		gameDisplay.blit(text, (width / 2 - widthT1 / 4 - 80, height / 2 - heightT1 / 2))
		gameDisplay.blit(text2, (width / 2 - 150, height / 2 + 100))
		x,y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Fechar o Game
				save_score(player)
				sys.exit()
		# Desenhando
		gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
		# Update 
		pygame.display.update()
		clock.tick(15)
# Game Loop
window = pygame.image.load("res/_ui/Window.png")
play = pygame.image.load("res/_ui/Play_BTN.png")
score = pygame.image.load("res/_ui/Score.png")
header = pygame.image.load("res/_ui/Header.png")
# Variaveis game-loop
def gameLoop():
	contadorTiros = 30
	contadorMeteoros = 50
	contadorVidas = 0
	contadorBoss = 0
	gameOn = True
	gamePause = False
	while gameOn:
		contadorTiros -= 1
		contadorMeteoros -= 1
		if contadorBoss > 0:
			contadorBoss -= 1
		if contadorVidas >= 0:
			contadorVidas -= 1
		# Eventos Game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save_score(player)
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.setAcceleration(-5)
				elif event.key == pygame.K_RIGHT:
					player.setAcceleration(5)
				if event.key == pygame.K_SPACE:
					if player.getShot() == None:
						player.doShoot()
						pygame.mixer.music.load("sounds/sfx_laser1.ogg")
						pygame.mixer.music.play()
				if event.key == pygame.K_p:
					if gamePause:
						gamePause = False
						gameLoop()
					else:
						gamePause = True
			elif event.type == pygame.KEYUP and player.getY() + player.getAcceleration() < height - 20:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					player.setAcceleration(0)
			# Tirar do Pause
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos()
				if mouseX >= 385 and mouseX <= 445 and mouseY >= 450 and mouseY <= 512:
					if gamePause:
						gameLoop()
						gamePause = False
		if not gamePause:
			# Atualizando Tiros
			for a in range(0,len(vetEnemies)):
				for b in range(0,len(vetEnemies[0])): 
					e = vetEnemies[a][b]
					if e != None:
						if e.getShot() != None:
							e.getShot().setY(e.getShot().getY()+e.getShot().getAcceleration())
							if e.getShot().getY() + e.getShot().getHeight() >= height:
								e.setShot(None)
			# Movimentação 
			vetEnemies2 = []
			if player.getX() + player.getAcceleration() - 10 < 0 and player.getAcceleration() == -5:
				player.setAcceleration(0)
			if player.getX() +  player.getWidth() + player.getAcceleration() + 10 > width - 10 and player.getAcceleration() == 5:
				player.setAcceleration(0)
			player.setX(player.getX() + player.getAcceleration())
			if player.getShot() != None:
				if player.getShot().getY() + player.getShot().getHeight() <= 0:
					player.setShot(None)
					if player.getScore() >= 10:
						player.setScore(player.getScore()-10)
				else:		
					shootVar = player.getShot()
					if shootVar != None:
						shootVar.setY(shootVar.getY() - shootVar.getAcceleration())
					# Colisão
					for a in range(0,len(vetEnemies)):
						for b in range(0,len(vetEnemies[0])):
							enemy = vetEnemies[a][b]
							if shootVar != None and vetEnemies[a][b] != None:
								if shootVar.getX() >= enemy.getX() and shootVar.getX() <= enemy.getX() + enemy.getWidth():
									if shootVar.getY() >= enemy.getY() and shootVar.getY() <= enemy.getY() + enemy.getHeight():
										vetEnemies[a][b] = None
										player.setScore(player.getScore()+50)									
										player.setShot(None)
			# Tiro Inimigos
			for a in range(0,len(vetEnemies)):
				for b in range(0,len(vetEnemies[0])):
					enemy = vetEnemies[a][b]
					if enemy != None:
						vetEnemies2.append(enemy)
			if len(vetEnemies2) >= 1:
				randomNumber = random.randint(1,len(vetEnemies2))-1
				# Tiro Aleatorio
				if vetEnemies2[randomNumber] != None:
					if vetEnemies2[randomNumber].getShot() == None and contadorTiros <= 0:
						vetEnemies2[randomNumber].doShoot()
						pygame.mixer.music.load("sounds/sfx_laser2.ogg")
						pygame.mixer.music.play()
						contadorTiros = 30
			# Meteoros
			if contadorMeteoros == 0:
				contadorMeteoros = 50
				m = Meteoro(-50,player.getY()-random.randrange(100,350))
				m.setImgSrc(vetMeteoros[random.randrange(0,2)])
				vetObjMeteoros.append(m)
			for meteoro in vetObjMeteoros:
				shootVar = player.getShot()
				if shootVar != None:
				# Meteoro colide com tiro do player
					if shootVar.getX() >= meteoro.getX() and shootVar.getX() <= meteoro.getX()+meteoro.getWidth()+10:
						if shootVar.getY() <= meteoro.getY() + meteoro.getHeight() and shootVar.getY() >= meteoro.getY() + meteoro.getHeight()/2:
							vetObjMeteoros.remove(meteoro) 
							player.setShot(None)	
							if player.getScore() >= 10:
								player.setScore(player.getScore()-10)
							# Tiro colide com boss
				# Meteoro colide com inimigo
				if meteoro in vetObjMeteoros:
					for enemy in vetEnemies2:
						shootVar = enemy.getShot()
						if shootVar != None:
							if shootVar.getX() >= meteoro.getX() and shootVar.getX() <= meteoro.getX()+meteoro.getWidth():
								if shootVar.getY() + shootVar.getHeight() >= meteoro.getY() + meteoro.getHeight():
									vetObjMeteoros.remove(meteoro)  
									enemy.setShot(None)													
				if (meteoro.getX() + meteoro.getWidth() < width):
					meteoro.setX(meteoro.getX()+meteoro.getAcceleration())
				else:
					vetObjMeteoros.remove(meteoro)
				if len(vetEnemies2) == 0:
					v = bossFinal.getTiros()
					for myVar in bossFinal.getTiros():
						myVar.setY(myVar.getY()+myVar.getAcceleration())
						if myVar.getX() >= player.getX() and myVar.getX() <= player.getX() + player.getHeight():
							if myVar.getY() + 57 >= player.getY() and myVar.getY() <= player.getY() + player.getHeight() and contadorVidas <= 0:
								player.setLife(player.getLife() - 1)
								pygame.mixer.music.load("sounds/tomoutiro.ogg")
								pygame.mixer.music.play()
								contadorVidas = 20
								if player.getLife() == 0:
									gameOver()
								v.remove(myVar)
								break
					bossFinal.setTiros(v)
					if bossFinal.getContadorTiros() == 0:
						randomInt = [bossFinal.getX()+70,bossFinal.getX()+170]
						t = Shoot(randomInt[random.randint(1,len(randomInt))-1], bossFinal.getY()+bossFinal.getHeight(), 9, 57, 5)
						v = bossFinal.getTiros()
						v.append(t)
						bossFinal.setTiros(v)
						bossFinal.setContadorTiros(150)
					else:
						bossFinal.setContadorTiros(bossFinal.getContadorTiros()-1)
					if bossFinal.getX() >= width - bossFinal.getWidth()  or bossFinal.getX() == 0:
						bossFinal.setVelocidade(bossFinal.getVelocidade()*-1)
					bossFinal.setX(bossFinal.getX()+bossFinal.getVelocidade())
					shootVar = player.getShot()
					if shootVar != None:
						if shootVar.getX() >= bossFinal.getX()+55 and shootVar.getX() <= bossFinal.getX() + bossFinal.getWidth() - 52:
							if shootVar.getY() <= bossFinal.getY() + bossFinal.getHeight() and shootVar.getY() >= bossFinal.getY():
								if contadorBoss == 0:
									bossFinal.setLife(bossFinal.getLife()-0.1)
									player.setScore(player.getScore() + 100)
									player.setShot(None)
					if bossFinal.getLife() >= 0 and bossFinal.getLife() < 0.1:
						gameOn = False
						pygame.mixer.music.load("sounds/Victory.ogg")
						pygame.mixer.music.play()
						gameWin()

				else:
					for x in vetEnemies2:
						if x.getShot() != None:
							nShoot = x.getShot()
							if nShoot.getX() >= player.getX() and nShoot.getX() <= player.getX() + player.getWidth():
								if nShoot.getY() + nShoot.getHeight() >= player.getY() and nShoot.getY() + nShoot.getHeight() <= player.getY() + player.getHeight():
										if contadorVidas <= 0:
											if player.getLife() == 1:
												gameOn = False
												newCoins = player.getCoins() + (player.getScore()//100)*player.getLife()
												player.setCoins(newCoins)
												save_score(player)
												# Musica fim 
												pygame.mixer.music.load("sounds/game-over.ogg")
												pygame.mixer.music.play()
												gameOver()
												break
											player.setLife(player.getLife() - 1)
											pygame.mixer.music.load("sounds/tomoutiro.ogg")
											pygame.mixer.music.play()
											contadorVidas = 20
										x.setShot(None)
				
		draw()
		if gamePause:
			gameDisplay.blit(window,(width/2-298/2,height/2-342/2))
			gameDisplay.blit(play,(width/2-130,height/2+90))
			gameDisplay.blit(header,(width/2-80,height/2-330/2))
			gameDisplay.blit(score,(width/2-130,height/2-220/2))
			size = len(str(player.getScore()))
			contador = 0
			for x in str(player.getScore()):
				gameDisplay.blit(vetImagens[int(x)], (width / 2 - 130 + (contador * 20), 280))
				contador += 1
			x,y = pygame.mouse.get_pos()
			gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
		pygame.display.update()
		clock.tick(fps) # Fps
# Carregando Background
bgImage = pygame.image.load("res/_backgrounds/blue.png") 
fps = 50
# Instrucoes na Tela
def gameInstrucoes():
	gameOn = False
	pygame.mixer.music.load("sounds/livro.ogg")
	pygame.mixer.music.play()
	while not gameOn:
		myFont1 = pygame.font.Font("sounds/kenvector_future.ttf", 45)
		myFont2 = pygame.font.Font("sounds/kenvector_future.ttf", 30)
		myFont3 = pygame.font.Font("sounds/kenvector_future.ttf", 15)
		text1= myFont1.render("Bem Vindos ao Space Shooters!", True, (0, 255, 0))
		text2 = myFont2.render("Teclas:", True, (255, 255, 255))
		text3 = myFont3.render("D => Direita", True, (255, 255, 255))
		text4 = myFont3.render("A => Esquerda", True, (255, 255, 255))
		text5 = myFont3.render("Spacebar => Atirar", True, (255, 255, 255))
		text6 = myFont2.render("Instrucoes Basicas:", True, (255, 255, 255))
		text7 = myFont3.render("1) Todo jogador começa com 3 vidas.", True, (255, 255, 255))
		text8 = myFont3.render("1.1) Caso o jogador queira mais vidas, ele poderá compra-las na loja com as moedas do jogo.", True, (255, 255, 255))
		text9 = myFont3.render("2) O objetivo do jogo é conseguir matar as naves inimigas e o Boss sem perder todas as suas vidas.", True, (255, 255, 255))
		text10 = myFont3.render("3) A cada 100 pontos no jogo o jogador recebe 1 moeda pra gastar na loja.", True, (255, 255, 255))
		text11 = myFont3.render("3.1) Com as moedas o jogador poderá comprar skins para nave,tiro, além de powerups para o jogo.", True, (255, 255, 255))
		text12 = myFont3.render("4) Caso o jogador perca todas as vidas antes do jogo acabar, uma tela de GAME OVER aparecerá.", True, (255, 255, 255))
		text13 = myFont3.render("5) Boa sorte! e Bom jogo!", True, (255, 255, 255))
		text14 = myFont2.render("Criado Por:", True, (255, 255, 255))
		text15 = myFont3.render("Leonardo Gideão", True, (0, 255, 0))
		text16 = myFont3.render("Thiago Z L Chaves", True, (0, 255, 0))
		text17 = myFont3.render("André Luiz", True, (0, 255, 0))
		while not gameOn:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: # FECHAR O GAME
					save_score(player)
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					x,y = pygame.mouse.get_pos()
					if x >= 915 and x <= 965 and y >= 610 and y <= 675:
							gameOn = True
							gameMenu()
							break
			# Fundo
			gameDisplay.fill((0,0,0))
			gameDisplay.blit(bgImage,(0,0))
			# Texto
			gameDisplay.blit(text1,(10,40))
			gameDisplay.blit(text2,(5,100))
			gameDisplay.blit(text3,(5,150))
			gameDisplay.blit(text4,(5,180))
			gameDisplay.blit(text5,(5,210))
			gameDisplay.blit(text6,(5,240))
			gameDisplay.blit(text7,(5,300))
			gameDisplay.blit(text8,(5,340))
			gameDisplay.blit(text9,(5,380))
			gameDisplay.blit(text10,(5, 420))
			gameDisplay.blit(text11,(5, 460))
			gameDisplay.blit(text12,(5, 500))
			gameDisplay.blit(text13,(5, 540))
			gameDisplay.blit(text14,(5, 580))
			gameDisplay.blit(text15,(5, 620))
			gameDisplay.blit(text16,(5, 640))
			gameDisplay.blit(text17,(5, 660))
			gameDisplay.blit(back,(width-110,height-110))
			# Desenhando Cursor
			x,y = pygame.mouse.get_pos()
			gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
			# Update
			pygame.display.update()
			clock.tick(15)
# Game Pause
def gameMenu():
	gameOn = False
	while not gameOn:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				save_score(player)
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseX, mouseY = pygame.mouse.get_pos() 
				if mouseX >= 390 and mouseX <= 609 and mouseY >= 330 and mouseY <= 365:
					gameOn = True
					gameLoop()
				if mouseX >= 390 and mouseX <= 609 and mouseY >= 384 and mouseY <= 417:
					gameOn = True
					gameInstrucoes()
				if mouseX >= 390 and mouseX <= 609 and mouseY >= 429 and mouseY <= 466:
					gameOn = True
					gameShop()
				pygame.mixer.music.load("sounds/click1.ogg")
				pygame.mixer.music.play()
		# Config Principais
		gameButton = [pygame.image.load("res/_ui/buttonYellow.png"), pygame.image.load("res/_ui/buttonRed.png"), pygame.image.load("res/_ui/buttonGreen.png"), pygame.image.load("res/_ui/buttonBlue.png") ] # 222 X 39 px
		pygame.font.init()
		myFont = pygame.font.Font("sounds/kenvector_future.ttf", 100)
		myFont2 = pygame.font.Font("sounds/Roboto-Black.ttf", 25)
		# Fundo na tela
		gameDisplay.blit(bgImage,(0,0))
		# Definindo Posicoes
		widthT1, heightT1 = myFont.size("Space")
		widthT2, heightT2 = myFont.size("Shooters")
		text = myFont.render("Space", True, (255, 255, 255))
		text2 = myFont.render("Shooters", True, (255, 255, 255))
		text3 = myFont2.render("Jogar Agora", True, (0, 0, 0))
		text4 = myFont2.render("Instruções", True, (0, 0, 0))
		text5 = myFont2.render("Loja", True, (0, 0, 0))
		# DESENHANDO NA TELA
		gameDisplay.blit(text,((width/2)-widthT1/2,20))
		gameDisplay.blit(text2,((width/2)-widthT2/2,heightT1+20))
		gameDisplay.blit(gameButton[0],(width/2 - 222/2,(height/2)-(39/2)))
		gameDisplay.blit(gameButton[1],(width/2 - 222/2,(height/2)-(39/2)+50*1))
		gameDisplay.blit(gameButton[2],(width/2 - 222/2,(height/2)-(39/2)+50*2))
		# TEXTOS
		gameDisplay.blit(text3,((width/2)-130/2,height/2-15))
		gameDisplay.blit(text4,((width/2)-120/2,height/2+35))
		gameDisplay.blit(text5,((width/2)-110/2,height/2+85))
		# Desenhando Cursor
		x,y = pygame.mouse.get_pos()
		gameDisplay.blit(cursorImg,(x-cursorImg.get_width()/2,y-cursorImg.get_height()/2))
		# Update 
		pygame.display.update()
		clock.tick(15)
# CONFIGS PADRÕES
gameDisplay = pygame.display.set_mode(size)
cursorImg = pygame.image.load("res/_ui/cursor.png").convert_alpha()
pygame.mouse.set_visible(False)
pygame.display.set_caption('Space Shooters')
clock = pygame.time.Clock() # Definindo atualizador do jogo
# Configurações 
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2)
# Main
if __name__ == "__main__":
	plx = read_score()
	player.setCoins(plx.getCoins())
	player.setShield(plx.getShield())
	player.setImgSrc(plx.getImgSrc())
	player.setLife(plx.getLife())
	playerImg = pygame.image.load(player.getImgSrc())
	gameMenu()
# Finalizando jogo
pygame.mixer.quit()
pygame.quit()
