import pygame

ANCHO = 800
ALTO = 600
TAMAÑO_CELDA = 20
VIDAS_INICIALES = 3
COLOR_FONDO = (0, 0, 0)
COLOR_TEXTO = (255, 255, 255)
COLOR_MANZANA = (255, 0, 0)  # Definimos el color de la manzana

NIVELES = [
    {"velocidad": 10, "obstaculos": 5},
    {"velocidad": 15, "obstaculos": 10},
    {"velocidad": 20, "obstaculos": 15}
]

def configurar_fuente():
    pygame.font.init()
    return pygame.font.Font(None, 36)

def configurar_sonido():
    pygame.mixer.init()
    sonido_manzana = pygame.mixer.Sound("sonidos/yoshi.mp3")
    sonido_nivel = pygame.mixer.Sound("sonidos/levelup.mp3")
    sonido_fin = pygame.mixer.Sound("sonidos/uhh.mp3")
    sonido_error = pygame.mixer.Sound("sonidos/uhh.mp3")
    return sonido_manzana, sonido_nivel, sonido_fin, sonido_error

def reproducir_musica_fondo():
    pygame.mixer.music.load("sonidos/musica.mp3")
    pygame.mixer.music.play(-1)

def detener_musica_fondo():
    pygame.mixer.music.stop()

def cargar_imagen(ruta):
    return pygame.image.load(ruta)

def reproducir_sonido(sonido):
    pygame.mixer.Sound.play(sonido)

def guardar_puntuacion(puntuacion):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"Puntuación: {puntuacion}\n")

def obtener_nivel(nivel):
    return NIVELES[nivel % len(NIVELES)]
