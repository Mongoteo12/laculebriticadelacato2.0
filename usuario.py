import configuracion

class Usuario:
    def __init__(self, nombre):
        """Inicializa un nuevo usuario con un nombre y estadísticas vacías."""
        self.nombre = nombre
        self.puntuacion_maxima = 0
        self.tiempo_juego = 0
        self.nivel_maximo = 0

    def actualizar_estadisticas(self, puntuacion, tiempo, nivel):
        """Actualiza las estadísticas del usuario."""
        if puntuacion > self.puntuacion_maxima:
            self.puntuacion_maxima = puntuacion
        self.tiempo_juego += tiempo
        if nivel > self.nivel_maximo:
            self.nivel_maximo = nivel

    def mostrar_estadisticas(self):
        """Muestra las estadísticas del usuario."""
        print(f"Usuario: {self.nombre}")
        print(f"Puntuación Máxima: {self.puntuacion_maxima}")
        print(f"Tiempo de Juego: {self.tiempo_juego}")
        print(f"Nivel Máximo: {self.nivel_maximo}")

class SistemaUsuarios:
    def __init__(self):
        """Inicializa el sistema de usuarios con una lista vacía de usuarios."""
        self.usuarios = []

    def agregar_usuario(self, nombre):
        """Agrega un nuevo usuario al sistema."""
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        return usuario

    def obtener_usuario(self, nombre):
        """Obtiene un usuario por su nombre."""
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None

    def mostrar_todos_usuarios(self):
        """Muestra todos los usuarios y sus estadísticas."""
        for usuario in self.usuarios:
            usuario.mostrar_estadisticas()

sistema_usuarios = SistemaUsuarios()
