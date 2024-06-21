import configuracion
import pygame

class Puntuaciones:
    def __init__(self):
        self.puntuaciones_altas = self.cargar_puntuaciones()

    def cargar_puntuaciones(self):
        puntuaciones = []
        try:
            with open("puntuaciones.txt", "r") as archivo:
                for linea in archivo:
                    try:
                        puntuaciones.append(int(linea.strip().split(": ")[-1]))
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass
        return sorted(puntuaciones, reverse=True)

    def guardar_puntuacion(self, puntuacion):
        self.puntuaciones_altas.append(puntuacion)
        self.puntuaciones_altas = sorted(self.puntuaciones_altas, reverse=True)
        with open("puntuaciones.txt", "w") as archivo:
            for puntuacion in self.puntuaciones_altas:
                archivo.write(f"Puntuación: {puntuacion}\n")

    def mostrar_puntuaciones(self, pantalla, fuente):
        pantalla.fill(configuracion.COLOR_FONDO)
        y = 100
        for puntuacion in self.puntuaciones_altas[:5]:
            texto = fuente.render(f"Puntuación: {puntuacion}", True, configuracion.COLOR_TEXTO)
            pantalla.blit(texto, (configuracion.ANCHO // 2 - 100, y))
            y += 40

puntuaciones = Puntuaciones()
