import configuracion

class Perfil:
    def __init__(self, usuario):
        """Inicializa el perfil del usuario con configuraciones predeterminadas."""
        self.usuario = usuario
        self.color_fondo = configuracion.COLOR_FONDO
        self.velocidad_juego = configuracion.VELOCIDAD_JUEGO
        self.tamaño_celda = configuracion.TAMAÑO_CELDA
        self.estadisticas = {
            'partidas_jugadas': 0,
            'puntuacion_maxima': 0,
            'tiempo_jugado': 0,
            'manzanas_comidas': 0
        }

    def actualizar_estadisticas(self, puntuacion, tiempo_jugado, manzanas_comidas):
        """Actualiza las estadísticas del perfil."""
        self.estadisticas['partidas_jugadas'] += 1
        self.estadisticas['tiempo_jugado'] += tiempo_jugado
        self.estadisticas['manzanas_comidas'] += manzanas_comidas
        if puntuacion > self.estadisticas['puntuacion_maxima']:
            self.estadisticas['puntuacion_maxima'] = puntuacion

    def cambiar_color_fondo(self, color):
        """Cambia el color de fondo del juego."""
        self.color_fondo = color
        configuracion.cambiar_color_fondo(color)

    def cambiar_velocidad_juego(self, velocidad):
        """Cambia la velocidad del juego."""
        self.velocidad_juego = velocidad
        configuracion.cambiar_velocidad_juego(velocidad)

    def cambiar_tamaño_celda(self, tamaño):
        """Cambia el tamaño de las celdas."""
        self.tamaño_celda = tamaño
        configuracion.cambiar_tamaño_celda(tamaño)

    def mostrar_configuracion(self):
        """Muestra la configuración actual del perfil."""
        print(f"Usuario: {self.usuario.nombre}")
        print(f"Color de Fondo: {self.color_fondo}")
        print(f"Velocidad del Juego: {self.velocidad_juego}")
        print(f"Tamaño de Celdas: {self.tamaño_celda}")
        print(f"Partidas Jugadas: {self.estadisticas['partidas_jugadas']}")
        print(f"Puntuación Máxima: {self.estadisticas['puntuacion_maxima']}")
        print(f"Tiempo Jugado: {self.estadisticas['tiempo_jugado']} segundos")
        print(f"Manzanas Comidas: {self.estadisticas['manzanas_comidas']}")

class SistemaPerfiles:
    def __init__(self):
        """Inicializa el sistema de perfiles con una lista de perfiles."""
        self.perfiles = []

    def agregar_perfil(self, usuario):
        """Agrega un nuevo perfil al sistema."""
        perfil = Perfil(usuario)
        self.perfiles.append(perfil)
        return perfil

    def obtener_perfil(self, usuario):
        """Obtiene un perfil por su usuario."""
        for perfil in self.perfiles:
            if perfil.usuario == usuario:
                return perfil
        return None

    def mostrar_todos_perfiles(self):
        """Muestra todos los perfiles y sus configuraciones."""
        for perfil in self.perfiles:
            perfil.mostrar_configuracion()

sistema_perfiles = SistemaPerfiles()
