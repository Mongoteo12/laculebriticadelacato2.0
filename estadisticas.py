import pygame
import configuracion

class Estadisticas:
    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self.tiempo_inicio = pygame.time.get_ticks()
        self.manzanas_comidas = 0
        self.niveles_completados = 0
        self.tiempo_juego = 0
        self.puntos_totales = 0
        self.vidas_restantes = configuracion.VIDAS_INICIALES

    def actualizar_manzanas_comidas(self):
        self.manzanas_comidas += 1

    def actualizar_niveles_completados(self):
        self.niveles_completados += 1

    def actualizar_tiempo_juego(self):
        self.tiempo_juego = (pygame.time.get_ticks() - self.tiempo_inicio) // 1000

    def actualizar_puntos_totales(self, puntos):
        self.puntos_totales += puntos

    def actualizar_vidas_restantes(self, vidas):
        self.vidas_restantes = vidas

    def registrar_juego(self, puntos, estado):
        with open("estadisticas_juegos.txt", "a") as file:
            file.write(f"Puntos: {puntos}, Estado: {estado}, Tiempo: {self.tiempo_juego}s, Manzanas: {self.manzanas_comidas}, Niveles: {self.niveles_completados}, Vidas: {self.vidas_restantes}\n")

    def mostrar_estadisticas(self, pantalla, fuente):
        self.actualizar_tiempo_juego()
        texto_tiempo = fuente.render(f"Tiempo: {self.tiempo_juego}s", True, configuracion.COLOR_TEXTO)
        texto_manzanas = fuente.render(f"Manzanas: {self.manzanas_comidas}", True, configuracion.COLOR_TEXTO)
        texto_niveles = fuente.render(f"Niveles: {self.niveles_completados}", True, configuracion.COLOR_TEXTO)
        texto_puntos = fuente.render(f"Puntos: {self.puntos_totales}", True, configuracion.COLOR_TEXTO)
        texto_vidas = fuente.render(f"Vidas: {self.vidas_restantes}", True, configuracion.COLOR_TEXTO)

        pantalla.blit(texto_tiempo, (10, 110))
        pantalla.blit(texto_manzanas, (10, 140))
        pantalla.blit(texto_niveles, (10, 170))
        pantalla.blit(texto_puntos, (10, 200))
        pantalla.blit(texto_vidas, (10, 230))

estadisticas = Estadisticas()
