import pygame
import configuracion

class Serpiente:
    def __init__(self):
        self.inicializar()

    def inicializar(self):
        self.posiciones = [(configuracion.ANCHO // 2, configuracion.ALTO // 2)]
        self.direccion = (0, -configuracion.TAMAÑO_CELDA)
        self.creciendo = False
        self.cabeza_imagen = configuracion.cargar_imagen("sonidos/yoshii.png")
        self.cuerpo_color = (0, 255, 0)

    def mover(self):
        cabeza_nueva = (self.posiciones[0][0] + self.direccion[0], self.posiciones[0][1] + self.direccion[1])
        if cabeza_nueva[0] < 0 or cabeza_nueva[0] >= configuracion.ANCHO or cabeza_nueva[1] < 0 or cabeza_nueva[1] >= configuracion.ALTO:
            raise Exception("La serpiente ha chocado con la pared")
        if not self.creciendo:
            self.posiciones.pop()
        else:
            self.creciendo = False
        self.posiciones.insert(0, cabeza_nueva)

    def cambiar_direccion(self, direccion):
        if (direccion[0] * -1, direccion[1] * -1) == self.direccion:
            return
        self.direccion = direccion

    def comer_manzana(self, posicion_manzana):
        if self.posiciones[0] == posicion_manzana:
            self.creciendo = True
            return True
        return False

    def comer_poder(self, posicion_poder):
        if self.posiciones[0] == posicion_poder:
            return True
        return False

    def chocar_con_cuerpo(self):
        return self.posiciones[0] in self.posiciones[1:]

    def dibujar(self, pantalla):
        for i, segmento in enumerate(self.posiciones):
            if i == 0:
                pantalla.blit(self.cabeza_imagen, segmento)
            else:
                pygame.draw.rect(pantalla, self.cuerpo_color, (*segmento, configuracion.TAMAÑO_CELDA, configuracion.TAMAÑO_CELDA))

serpiente = Serpiente()
