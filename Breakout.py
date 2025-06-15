from pygame import *
from random import randint

init()
SW, SH = 800, 600
FPS = 60
window = display.set_mode((SW, SH))
display.set_caption('Breakout')

BACKGROUND = "background.png"
PALETTE_IMG = "player1.png"  
BOLA_IMG = "bola.png"
VICTORY_IMG = "victoryplayer1.png"
BLOQUE_IMG1 = "rectangulo.png" 
BLOQUE_IMG2 = "rectangulo2.png" 
BLOQUE_IMG3 = "rectangulo3.png" 

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < SW - self.rect.width:
            self.rect.x += self.speed
            
class Block(GameSprite):
    def __init__(self, x, y, width, height, img):
        super().__init__(img, x, y, width, height)

def random_sign():
    return 1 if randint(0, 1) == 1 else -1
    
paleta = Player(PALETTE_IMG, SW // 2 - 60, SH - 40, 120, 20, speed=10)
bola = GameSprite(BOLA_IMG, SW // 2, SH // 2, 30, 30)

speed_x = 6 * random_sign()
speed_y = -6

bloques = sprite.Group()
filas = 6
columnas = 6
bloque_ancho = SW // columnas
bloque_alto = 30

def create_blocks():
    for fila in range(filas):
        for col in range(columnas):
            x = col * bloque_ancho
            y = fila * bloque_alto + 50
            grupo = (fila // 2) % 3
            if grupo == 0:
                img = BLOQUE_IMG1
            elif grupo == 1:
                img = BLOQUE_IMG2
            else:
                img = BLOQUE_IMG3
            # Los bloques son ligeramente más pequeños para que haya un espacio entre ellos
            bloque = Block(x, y, bloque_ancho - 2, bloque_alto - 2, img) 
            bloques.add(bloque)

create_blocks() 

font.init()
font_gameover = font.SysFont('Arial', 72)
font_score = font.SysFont('Arial', 36)

score = 0
clock = time.Clock()
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        paleta.update()

        bola.rect.x += speed_x
        bola.rect.y += speed_y

        # Rebotar en los bordes de la pantalla (izquierdo/derecho)
        if bola.rect.left <= 0 or bola.rect.right >= SW:
            speed_x *= -1
        # Rebotar en el borde superior
        if bola.rect.top <= 0:
            speed_y *= -1

        # Colisión de la bola con la paleta
        if bola.rect.colliderect(paleta.rect) and speed_y > 0: # Solo si la bola viene de arriba hacia abajo
            speed_y *= -1
            # Ajustar el rebote según dónde golpea la paleta
            offset = (bola.rect.centerx - paleta.rect.centerx) / (paleta.rect.width / 2)
            speed_x = 6 * offset

        # Colisión de la bola con los bloques
        bloque_colision = sprite.spritecollideany(bola, bloques)
        if bloque_colision:
            bloques.remove(bloque_colision)
            speed_y *= -1
            score += 1

        # Si la bola cae por debajo de la pantalla
        if bola.rect.top > SH:
            finish = True

        # Si no quedan bloques
        if len(bloques) == 0:
            finish = True

        # Dibujar elementos del juego
        window.blit(transform.scale(image.load(BACKGROUND), (SW, SH)), (0, 0))
        paleta.reset()
        bola.reset()
        bloques.draw(window) # Dibuja todos los sprites del grupo de bloques

        # Mostrar puntuación
        score_text = font_score.render(f"Puntos: {score}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))

    else: # Juego terminado (ganado o perdido)
        if len(bloques) == 0:
            texto = font_gameover.render("¡Ganaste!", True, (0, 255, 0))
        else:
            texto = font_gameover.render("¡Perdiste!", True, (255, 0, 0))
        window.blit(texto, (SW // 2 - texto.get_width() // 2, SH // 2 - texto.get_height() // 2))

        texto_reiniciar = font_score.render("Presiona R para reiniciar", True, (255, 255, 255))
        window.blit(texto_reiniciar, (SW // 2 - texto_reiniciar.get_width() // 2, SH // 2 + 80))

        keys = key.get_pressed()
        if keys[K_r]: # Tecla 'R' para reiniciar
            # Reiniciar la posición de la bola y la paleta
            bola.rect.center = (SW // 2, SH // 2)
            speed_x = 6 * random_sign()
            speed_y = -6
            paleta.rect.centerx = SW // 2 # Centrar la paleta
            
            # Limpiar y recrear los bloques
            bloques.empty()
            create_blocks() # Volver a llamar a la función para recrear los bloques
            
            score = 0
            finish = False

    display.update()
    clock.tick(FPS)

quit()
