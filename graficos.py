import configuracion

class Graficos:
    def __init__(self):
        """Inicializa la configuración gráfica del juego."""
        self.resolucion = (configuracion.ANCHO, configuracion.ALTO)
        self.calidad_textura = "Alta"

    def cambiar_resolucion(self, ancho, alto):
        """Cambia la resolución del juego."""
        self.resolucion = (ancho, alto)
        configuracion.ANCHO = ancho
        configuracion.ALTO = alto

    def cambiar_calidad_textura(self, calidad):
        """Cambia la calidad de las texturas."""
        self.calidad_textura = calidad

    def mostrar_configuracion_grafica(self):
        """Muestra la configuración gráfica actual."""
        print(f"Resolución: {self.resolucion[0]}x{self.resolucion[1]}")
        print(f"Calidad de Textura: {self.calidad_textura}")

graficos = Graficos()
