import configuracion

class SistemaNiveles:
    def __init__(self):
        self.niveles = self.crear_niveles()

    def crear_niveles(self):
        niveles = []
        for i, config in enumerate(configuracion.NIVELES):
            nivel = {
                "numero": i + 1,
                "velocidad": config["velocidad"],
                "obstaculos": config["obstaculos"]
            }
            niveles.append(nivel)
        return niveles

    def obtener_nivel(self, numero):
        if 0 <= numero < len(self.niveles):
            return self.niveles[numero]
        else:
            return self.niveles[-1]  # Devolver el último nivel si el número está fuera del rango

sistema_niveles = SistemaNiveles()
