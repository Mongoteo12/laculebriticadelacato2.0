import pygame
import configuracion
import random

class Manzana:
    def __init__(self):
        self.generar_nueva()

    def generar_nueva(self):
        self.posicion = (
            random.randint(0, (configuracion.ANCHO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA,
            random.randint(0, (configuracion.ALTO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA
        )

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, configuracion.COLOR_MANZANA, (*self.posicion, configuracion.TAMAÑO_CELDA, configuracion.TAMAÑO_CELDA))

manzana = Manzana()
