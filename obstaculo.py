import pygame
import random
import configuracion

class Obstaculo:
    def __init__(self):
        self.generar_nuevo()

    def generar_nuevo(self):
        self.posicion = (
            random.randint(0, (configuracion.ANCHO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA,
            random.randint(0, (configuracion.ALTO - configuracion.TAMAÑO_CELDA) // configuracion.TAMAÑO_CELDA) * configuracion.TAMAÑO_CELDA
        )

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, configuracion.COLOR_OBSTACULO, (*self.posicion, configuracion.TAMAÑO_CELDA, configuracion.TAMAÑO_CELDA))

# No se debe instanciar aquí para evitar confusión en otros módulos
# obstaculo = Obstaculo()
