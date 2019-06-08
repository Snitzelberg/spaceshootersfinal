from player import Player
def save_score(player):
    try:
        f = open('game_save.txt', 'r')
        x = f.readline().split("#")
        hs = int(x[0])
        if hs < player.getScore():
            hs = player.getScore()
        stringFinal = str(hs)+"#"+str(player.getCoins())+"#"+str(player.getShield())+"#"+str(player.getImgSrc())+"#"+str(x[4])
        arquivoTxt = open("game_save.txt",'w')
        arquivoTxt.write(stringFinal)
        arquivoTxt.close()
    except:
        print("Erro de arquivo: contate o programador do codigo")
def save_life(player):
    try:
        f = open('game_save.txt', 'r')
        x = f.readline().split("#")
        stringFinal = x[0]+"#"+x[1]+"#"+x[2]+"#"+x[3]+"#"+str(player.getLife())
        arquivoTxt = open("game_save.txt",'w')
        arquivoTxt.write(stringFinal)
        arquivoTxt.close()
    except:
        print("Erro de arquivo: contate o programador do codigo")
def read_score():
    f = open('game_save.txt','r')
    x = f.readline().split("#")
    player = Player()
    player.setCoins(int(x[1]))
    player.setImgSrc(x[3])
    player.setLife(int(x[4]))
    if x[2] == 'True':
        player.setShield(True)
    else:
        player.setShield(False)
    return player