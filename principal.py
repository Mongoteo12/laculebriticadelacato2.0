from juego import bucle_juego
from menu import mostrar_menu
from opciones import mostrar_opciones
from puntuaciones import puntuaciones
from usuario import sistema_usuarios, Usuario
from nivel import sistema_niveles
from estadisticas import estadisticas
from interfaz_usuario import InterfazUsuario
import pygame
import configuracion
from nivel import sistema_niveles   

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    interfaz = InterfazUsuario(pantalla, fuente)

    usuario_actual = None

    while True:
        if not usuario_actual:
            nombre = interfaz.obtener_nombre_usuario()
            usuario_actual = sistema_usuarios.agregar_usuario(nombre)

        opcion = mostrar_menu()
        if opcion == "jugar":
            bucle_juego(usuario_actual)
        elif opcion == "opciones":
            mostrar_opciones()
        elif opcion == "puntuaciones":
            mostrar_puntuaciones_altas()
        elif opcion == "usuarios":
            sistema_usuarios.mostrar_todos_usuarios()
        elif opcion == "niveles":
            sistema_niveles.mostrar_todos_niveles()
        elif opcion == "estadisticas":
            estadisticas.mostrar_estadisticas()

def mostrar_puntuaciones_altas():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    pantalla.fill(configuracion.COLOR_FONDO)
    puntuaciones.mostrar_puntuaciones(pantalla, fuente)
    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN or evento.type == pygame.QUIT:
                esperando = False

if __name__ == "__main__":
    main()
