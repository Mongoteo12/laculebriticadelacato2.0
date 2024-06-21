


import pygame

def configurar_sonido():
    """Configura los sonidos del juego."""
    pygame.mixer.init()
    sonido_manzana = pygame.mixer.Sound("sonidos/yoshi.mp3")
    sonido_nivel = pygame.mixer.Sound("sonidos/levelup.mp3")
    sonido_fin = pygame.mixer.Sound("sonidos/uhh.mp3")
    sonido_error = pygame.mixer.Sound("sonidos/uhh.mp3")
    return sonido_manzana, sonido_nivel, sonido_fin, sonido_error


def reproducir_musica_fondo():
    """Reproduce música de fondo."""
    pygame.mixer.music.load("sonidos/musica.mp3")
    pygame.mixer.music.play(-1)  # Repite la música indefinidamente

def detener_musica_fondo():
    """Detiene la música de fondo."""
    pygame.mixer.music.stop()

