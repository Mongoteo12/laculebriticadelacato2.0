import pygame
import random
import configuracion

class Poder:
    def __init__(self):
        self.tipo = random.choice(["velocidad", "puntos", "invencibilidad"])
        self.generar_nueva()

    def generar_nueva(self):
        self.posicion = (
            random.randint(0, (configuracion.ANCHO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA,
            random.randint(0, (configuracion.ALTO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA
        )
        self.tipo = random.choice(["velocidad", "puntos", "invencibilidad"])

    def aplicar_efecto(self, juego):
        if self.tipo == "velocidad":
            juego.velocidad_temporal = True
            juego.tiempo_efecto = pygame.time.get_ticks()
        elif self.tipo == "puntos":
            juego.puntuacion += 50
        elif self.tipo == "invencibilidad":
            juego.invencibilidad_temporal = True
            juego.tiempo_efecto = pygame.time.get_ticks()

    def dibujar(self, pantalla):
        color = (0, 0, 255) if self.tipo == "velocidad" else (255, 255, 0) if self.tipo == "puntos" else (255, 0, 255)
        pygame.draw.rect(pantalla, color, (*self.posicion, configuracion.TAMAÑO_CELDA, configuracion.TAMAÑO_CELDA))

poder = Poder()
