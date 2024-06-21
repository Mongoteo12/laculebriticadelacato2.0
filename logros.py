import pygame
import configuracion

class Logros:
    def __init__(self):
        self.logros = []
        self.logros_desbloqueados = []

    def verificar_logros(self, puntuacion, tiempo, nivel, manzanas):
        nuevos_logros = []
        if puntuacion >= 100 and "Puntuación Alta" not in self.logros_desbloqueados:
            nuevos_logros.append("Puntuación Alta")
            self.logros_desbloqueados.append("Puntuación Alta")
        if tiempo <= 60 and "Tiempo Rápido" not in self.logros_desbloqueados:
            nuevos_logros.append("Tiempo Rápido")
            self.logros_desbloqueados.append("Tiempo Rápido")
        if nivel >= 5 and "Nivel Experto" not in self.logros_desbloqueados:
            nuevos_logros.append("Nivel Experto")
            self.logros_desbloqueados.append("Nivel Experto")
        if manzanas >= 10 and "Manzana Maestro" not in self.logros_desbloqueados:
            nuevos_logros.append("Manzana Maestro")
            self.logros_desbloqueados.append("Manzana Maestro")

        self.logros.extend(nuevos_logros)
        return nuevos_logros

    def mostrar_logros(self, pantalla, fuente):
        y_offset = 550
        for logro in self.logros:
            texto_logro = fuente.render(logro, True, configuracion.COLOR_TEXTO)
            pantalla.blit(texto_logro, (10, y_offset))
            y_offset += 30

    def mostrar_notificacion(self, pantalla, fuente, logro):
        texto_notificacion = fuente.render(f"Logro Desbloqueado: {logro}", True, configuracion.COLOR_TEXTO)
        pantalla.blit(texto_notificacion, (configuracion.ANCHO // 2 - 150, configuracion.ALTO // 2))

logros = Logros()
