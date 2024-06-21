class Recompensa:
    def __init__(self, tipo, valor):
        """Inicializa una recompensa con un tipo y un valor."""
        self.tipo = tipo
        self.valor = valor

    def mostrar_recompensa(self):
        """Muestra la información de la recompensa."""
        print(f"Recompensa de tipo {self.tipo} con valor de {self.valor}")

class SistemaRecompensas:
    def __init__(self):
        """Inicializa el sistema de recompensas con una lista de recompensas."""
        self.recompensas = []

    def agregar_recompensa(self, tipo, valor):
        """Agrega una nueva recompensa al sistema."""
        recompensa = Recompensa(tipo, valor)
        self.recompensas.append(recompensa)

    def mostrar_todas_recompensas(self):
        """Muestra todas las recompensas en el sistema."""
        for recompensa in self.recompensas:
            recompensa.mostrar_recompensa()

    def obtener_recompensas_por_tipo(self, tipo):
        """Obtiene todas las recompensas de un tipo específico."""
        return [recompensa for recompensa in self.recompensas if recompensa.tipo == tipo]

sistema_recompensas = SistemaRecompensas()

# Añadiendo algunas recompensas predeterminadas
sistema_recompensas.agregar_recompensa("Logro", "Puntuación 100")
sistema_recompensas.agregar_recompensa("Logro", "Nivel 5")
sistema_recompensas.agregar_recompensa("Logro", "50 manzanas comidas")
sistema_recompensas.agregar_recompensa("Logro", "10 minutos de juego")
