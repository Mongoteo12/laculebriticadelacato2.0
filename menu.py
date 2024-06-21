import pygame
import configuracion

def mostrar_menu():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()

    opciones = ["Jugar", "Opciones", "Puntuaciones", "Usuarios", "Niveles", "Estadísticas", "Perfil", "Recompensas", "Gráficos", "Salir"]
    seleccion = 0

    while True:
        pantalla.fill(configuracion.COLOR_FONDO)
        
        for i, opcion in enumerate(opciones):
            color = configuracion.COLOR_TEXTO if i != seleccion else (255, 0, 0)
            texto = fuente.render(opcion, True, color)
            pantalla.blit(texto, (configuracion.ANCHO // 2 - 100, 100 + i * 50))
        
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                if evento.key == pygame.K_RETURN:
                    return opciones[seleccion].lower()
