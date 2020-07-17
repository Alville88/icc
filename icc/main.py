import pygame
import random
import time
import datetime
pygame.init()
win = pygame.display.set_mode((700,700))  #Configuracion basica de ventana
pygame.display.set_caption("Covid Run")
reloj = pygame.time.Clock()

covid = pygame.image.load("covid.png")
humanito = pygame.image.load("humanito.png") # Sacar imagenes de archivo
humanito2 = pygame.image.load("humanito2.png")
mascarillita = pygame.image.load("mascarilla.png")
calle = pygame.image.load("calle.png")
caratula = pygame.image.load("caratulainicio.png")
caratulafinal = pygame.image.load("caratulafinal.png")
sonidotoz = pygame.mixer.Sound("toz2.wav") #sacar sonidos
sonidopresi = pygame.mixer.Sound("presi.wav")
musicainicio = pygame.mixer.music.load("enpartida.mp3")
pygame.mixer.music.set_volume(0.01)
#musicapartida = pygame.mixer.sound("enpartida.mp3")

class jugador(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        #self.contapasos = 0
        self.visible = True
        self.hitbox = (self.x, self.y, 90, 50)

    def draw(self, win):
        global tiempo
        global personaje
        #datetime.datetime.now().microsecond % 2
        if(abs(datetime.datetime.now().microsecond - tiempo) > 150000 and personaje == humanito):
            tiempo = datetime.datetime.now().microsecond
            personaje = humanito2

        elif (abs(datetime.datetime.now().microsecond - tiempo) > 150000 and personaje == humanito2):
            tiempo = datetime.datetime.now().microsecond
            personaje = humanito

            #win.blit(humanito2, (self.x, self.y)) #para que se dibuje la imagen en la pantalla
        #pygame.draw.rect(win, (255,0,0), (self.x, self.y, 90, 50))
        self.hitbox = (self.x, self.y, 90, 50)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        win.blit(personaje, (self.x, self.y)) #para que se dibuje la imagen en la pantalla

    def hit(self):
        #self.x = 325
        #self.y = 600
        #self.contapasos = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("-1 VIDA", 1, (255,0,0)) #el 1 es antialiasing
        textS = font1.render("-1 VIDA", 1, (0, 0, 0))
        win.blit(textS, (223.5, 203.5))
        win.blit(text, (220, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Esta parte pone una condicion para que el delay no ocurra cuando aprietas el boton de salir
                    i = 301
                    pygame.quit()

class viruses(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.end = end
        self.path = (self.x, self.end)
        #self.contapasos = 0
        self.vel = 5
        self.x = random.randrange(0,700)
        self.hitbox = (self.x, self.y, 50, 50)


    def draw(self,win):
            #cambiar si no funca
        self.move()
        self.hitbox = (self.x, self.y, 50, 57)
        #pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 50 ))
        win.blit(covid, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 50)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self): #Esto controla el movimiento en el path para si llega a un limite se da vuelta y cambia de direccion
        if self.vel > 0:
            if self.x + self.vel < self.path[1]: #Esto hace que el personaje solo se mueve si esta dentro de self.path que son los limites
                self.y += self.vel


class mascarillas(object):
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.end = end
        self.path = (self.x, self.end)
        self.vel = 3
        self.x = random.randrange(0,700)
        self.y = -1000 - random.randrange(500,3000) #donde aparece la mascarilla
        self.hitbox = (self.x, self.y, 50, 50)

    def draw(self,win):
        self.move()
        self.hitbox = (self.x, self.y, 50, 57)
        #pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 50 ))
        win.blit(mascarillita, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 50)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self): #Esto controla el movimiento en el path para si llega a un limite se da vuelta y cambia de direccion
        if self.vel > 0:
            if self.x + self.vel < self.path[1]: #Esto hace que el personaje solo se mueve si esta dentro de self.path que son los limites
                self.y += self.vel

    def hit(self):
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("+1 VIDA", 1, (15,200,240))
        text2 = font1.render("+1 VIDA", 1, (255, 255, 255))
        win.blit(text2, (203, 203))
        win.blit(text, (200, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()



"""def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)"""


def pprincipal():
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        font1 = pygame.font.SysFont("comicsans", 100)
        textmenu = font1.render("COVID RUN", 1, (0,200,0))

        maxp = open("highscore.txt", "r")
        puntajemax = maxp.readline()
        font2 = pygame.font.SysFont("comicsans", 50)
        #highscore = font2.render(f"Puntuación máxima: {str(puntajemax)}", 1, (15,200,240))

        win.blit(caratula, (-3,0))
        #win.blit(textmenu, (160, 200))
        #win.blit(highscore, (300, 500))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    #musicapartida.play()
def pausa():
    pause = True
    while pause:
        font1 = pygame.font.SysFont("comicsans", 100)
        textmenu = font1.render("PAUSA", 1, (0,200,0))

        font2 = pygame.font.SysFont("comicsans", 50)
        pausado = font2.render("presiona r para continuar", 1, (15,200,0))
        win.blit(pausado, (150, 300))
        win.blit(textmenu, (250, 200))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    pause = False
                    pygame.time.delay(1000)
def gameover():
    global masaltapuntuacion
    global puntajeactual
    over = True
    maxp = open("highscore.txt", "r")
    puntajemax = maxp.readline()
    while over:
        font1 = pygame.font.SysFont("comicsans", 100)
        textmenu = font1.render("GAME OVER", 1, (245,0,0))
        textmenu2 = font1.render("GAME OVER", 1, (0,0,0))
        font2 = pygame.font.SysFont("comicsans", 50)
        reiniciar = font2.render("presione x para reiniciar", 1, (15,200,240))
        reiniciar2 = font2.render("presione x para reiniciar", 1, (0,0,0))

        font2 = pygame.font.SysFont("comicsans", 50)
        highscore = font2.render(f"Puntuación máxima: {str(puntajemax)}", 1, (163,73,164))

        currentscore = font2.render(f"Puntuación actual: {str(puntajeactual)}", 1, (163,73,164))

        win.fill((255,255,255))
        win.blit(caratulafinal, (0,0))
        win.blit(reiniciar2, (151, 351))
        win.blit(reiniciar, (150, 350))
        win.blit(textmenu2, (136, 271))
        win.blit(textmenu, (135, 273))
        win.blit(currentscore, (165, 400))
        win.blit(highscore, (150, 450))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    over = False
def maxpuntaje ():
    global masaltapuntuacion
    puntuacionmaxima = open("highscore.txt", "w")
    puntuacionmaxima.write(str(masaltapuntuacion))
    print(masaltapuntuacion)
    puntuacionmaxima.close()

def redrawGameWindow():
    win.blit(calle, (0,0))
    hombre.draw(win)
    virus.draw(win)
    virus2.draw(win)
    virus3.draw(win)
    mascarilla1.draw(win)
    textvidas = font.render("Vidas: " + str(vidas), 1, (255,255,255))
    textvidas2= font.render("Vidas: " + str(vidas), 1, (0,0,0))
    puntos = font.render("Puntaje: " + str(puntaje), 1, (255,255,255))
    puntos2 = font.render("Puntaje: " + str(puntaje), 1, (0,0,0))
    win.blit(puntos, (550,10))
    win.blit(puntos2, (549,9))
    win.blit(textvidas, (10, 10))
    win.blit(textvidas2, (9, 9))
    pygame.display.update()

cont = 0
virus = viruses(50,0,100,100,700)
virus2 = viruses(50,0,100,150,700)
virus3 = viruses(50,0,100,150,700)
mascarilla1 = mascarillas(50,0,100,150,700)
font = pygame.font.SysFont("comicsans", 30, True, True)
introduccion = pprincipal()
#puntajeinicial = inicioscore()
personaje = humanito
tiempo = datetime.datetime.now().microsecond
tiempo1 = -1
#tiempo2 = -1
#tiempo3 = -1
tiempo4 = -1
puntaje = 0
masaltapuntuacion = 0
numviruses = [virus,virus2,virus3]
vidas = 3
empezar = 0
hombre = jugador(325, 600, 90, 50)
corre = True
while corre: #MAIN LOOOOOP

    reloj.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corre = False
    teclas = pygame.key.get_pressed()

#self.hitbox = (self.x, self.y, 50, 50)

    for covi in numviruses:
        if pygame.time.get_ticks() > tiempo1+2000:
            if hombre.hitbox[1] < covi.hitbox[1] + covi.hitbox[3] and hombre.hitbox[1] + hombre.hitbox[3] > covi.hitbox[1]:
                if hombre.hitbox[0] + hombre.hitbox[2] > covi.hitbox[0] and hombre.hitbox[0] < covi.hitbox[0] + covi.hitbox[2]:
                    sonidotoz.play()
                    hombre.hit()
                    tiempo1 = pygame.time.get_ticks()
                    vidas -= 1


    """if pygame.time.get_ticks() > tiempo1+2000:
        if hombre.hitbox[1] < virus.hitbox[1] + virus.hitbox[3] and hombre.hitbox[1] + hombre.hitbox[3] > virus.hitbox[1]:
            if hombre.hitbox[0] + hombre.hitbox[2] > virus.hitbox[0] and hombre.hitbox[0] < virus.hitbox[0] + virus.hitbox[2]:
                sonidotoz.play()
                hombre.hit()
                tiempo1 = pygame.time.get_ticks()
                vidas -= 1

    if pygame.time.get_ticks() > tiempo2+2000:
        if hombre.hitbox[1] < virus2.hitbox[1] + virus2.hitbox[3] and hombre.hitbox[1] + hombre.hitbox[3] > virus2.hitbox[1]:
            if hombre.hitbox[0] + hombre.hitbox[2] > virus2.hitbox[0] and hombre.hitbox[0] < virus2.hitbox[0] + virus2.hitbox[2]:
                sonidotoz.play()
                hombre.hit()
                tiempo2 = pygame.time.get_ticks()
                vidas -= 1

    if pygame.time.get_ticks() > tiempo3+2000:
        if hombre.hitbox[1] < virus3.hitbox[1] + virus3.hitbox[3] and hombre.hitbox[1] + hombre.hitbox[3] > virus3.hitbox[1]:
            if hombre.hitbox[0] + hombre.hitbox[2] > virus3.hitbox[0] and hombre.hitbox[0] < virus3.hitbox[0] + virus3.hitbox[2]:
                sonidotoz.play()
                hombre.hit()
                tiempo3 = pygame.time.get_ticks()
                vidas -= 1"""


    if pygame.time.get_ticks() > tiempo4+2000:
        if hombre.hitbox[1] < mascarilla1.hitbox[1] + mascarilla1.hitbox[3] and hombre.hitbox[1] + hombre.hitbox[3] > mascarilla1.hitbox[1]:
            if hombre.hitbox[0] + hombre.hitbox[2] > mascarilla1.hitbox[0] and hombre.hitbox[0] < mascarilla1.hitbox[0] + mascarilla1.hitbox[2]:
                sonidopresi.play()
                mascarilla1.hit()
                tiempo4 = pygame.time.get_ticks()
                vidas += 1

    #Para que los virus no esten enciuma de los otros
    if virus.hitbox[1] < virus2.hitbox[1] + virus2.hitbox[3] and virus.hitbox[1] + virus.hitbox[3] > virus2.hitbox[1]:
        if virus.hitbox[0] + virus.hitbox[2] > virus2.hitbox[0] and virus.hitbox[0] < virus2.hitbox[0] + virus2.hitbox[2]:
            virus.x = random.randrange(0,650)

    if virus.hitbox[1] < virus3.hitbox[1] + virus3.hitbox[3] and virus.hitbox[1] + virus.hitbox[3] > virus3.hitbox[1]:
        if virus.hitbox[0] + virus.hitbox[2] > virus3.hitbox[0] and virus.hitbox[0] < virus3.hitbox[0] + virus3.hitbox[2]:
            virus.x = random.randrange(0,650)

    if virus2.hitbox[1] < virus3.hitbox[1] + virus3.hitbox[3] and virus2.hitbox[1] + virus2.hitbox[3] > virus3.hitbox[1]:
        if virus2.hitbox[0] + virus2.hitbox[2] > virus3.hitbox[0] and virus2.hitbox[0] < virus3.hitbox[0] + virus3.hitbox[2]:
            virus2.x = random.randrange(0,650)

    if mascarilla1.y > 700:
        mascarilla1.y = -1000 - random.randrange(1000,2500)
        mascarilla1.x = random.randrange(0,650)

    for covi in numviruses: #modificacion el el y para que no esten juntitos
        if covi.y > 700:
            puntaje += 1
            covi.y = 0-random.randrange(50,100)
            covi.x = random.randrange(0,650)

    """if virus.y > 700:
        puntaje += 1
        virus.y = -50
        virus.x = random.randrange(0,650)

    if virus2.y > 700:
        puntaje += 1
        virus2.y = -50
        virus2.x = random.randrange(0,650)

    if virus3.y > 700:
        puntaje += 1
        virus3.y = -50
        virus3.x = random.randrange(0,650)"""

    for covis in numviruses:
        if pygame.time.get_ticks() > 10000:
            covis.vel += 0.001

    """if pygame.time.get_ticks() > 10000:
        virus.vel += 0.001

    if pygame.time.get_ticks() > 11000:
        virus2.vel += 0.001

    if pygame.time.get_ticks() > 12000:
        virus3.vel += 0.001"""

    if teclas[pygame.K_RIGHT] and hombre.x < 700 - hombre.width - hombre.vel:
        hombre.x += hombre.vel

    elif teclas[pygame.K_LEFT] and hombre.x > hombre.vel:
        hombre.x -= hombre.vel
    #else:
        #hombre.contapasos = 0
    if teclas[pygame.K_p]:
        pausa()
    if teclas[pygame.K_m]:
        pygame.mixer.music.pause()
    if teclas[pygame.K_q]:
        pygame.mixer.music.unpause()
    puntajeactual = puntaje
    if vidas == 0:
        maxp = open("highscore.txt", "r")
        masaltapuntuacion = int(maxp.readline().split()[0])
        if puntaje > masaltapuntuacion:
            masaltapuntuacion = puntaje
            maxpuntaje ()
        virus = viruses(50,0,100,100,700)
        virus2 = viruses(50,0,100,150,700)
        virus3 = viruses(50,0,100,150,700)
        mascarilla1 = mascarillas(50,0,100,150,700)
        font = pygame.font.SysFont("comicsans", 30, True, True)
        tiempo1 = -1
        #tiempo2 = -1
        #tiempo3 = -1
        tiempo4 = -1
        puntaje = 0
        numviruses = [virus,virus2,virus3]
        vidas = 3
        empezar = 0
        hombre = jugador(325, 600, 90, 50)
        corre = True
        pygame.time.delay(500)
        gameover()
        maxpuntaje ()

    #win.fill((250,250,250))
    redrawGameWindow()
pygame.quit()
