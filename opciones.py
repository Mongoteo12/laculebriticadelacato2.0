import pygame
import configuracion
import sonidos

def mostrar_opciones():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()

    opciones = ["Color Fondo", "Tamaño Celdas", "Dificultad", "Sonido", "Volver"]
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
                    if seleccion == 0:
                        mostrar_seleccion_color_fondo()
                    elif seleccion == 1:
                        mostrar_seleccion_tamaño_celdas()
                    elif seleccion == 2:
                        mostrar_seleccion_dificultad()
                    elif seleccion == 3:
                        mostrar_seleccion_sonido()
                    elif seleccion == 4:
                        return

def mostrar_seleccion_color_fondo():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    colores_fondo = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0)]
    nombres_colores = ["Negro", "Blanco", "Azul", "Verde", "Rojo"]
    seleccion = 0

    while True:
        pantalla.fill(configuracion.COLOR_FONDO)
        
        for i, color_nombre in enumerate(nombres_colores):
            color = configuracion.COLOR_TEXTO if i != seleccion else (255, 0, 0)
            texto = fuente.render(color_nombre, True, color)
            pantalla.blit(texto, (configuracion.ANCHO // 2 - 100, 100 + i * 50))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(nombres_colores)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(nombres_colores)
                if evento.key == pygame.K_RETURN:
                    configuracion.cambiar_color_fondo(colores_fondo[seleccion])
                    return

def mostrar_seleccion_tamaño_celdas():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    tamaños_celdas = [10, 20, 30]
    seleccion = 1

    while True:
        pantalla.fill(configuracion.COLOR_FONDO)
        
        for i, tamaño in enumerate(tamaños_celdas):
            color = configuracion.COLOR_TEXTO if i != seleccion else (255, 0, 0)
            texto = fuente.render(str(tamaño), True, color)
            pantalla.blit(texto, (configuracion.ANCHO // 2 - 100, 100 + i * 50))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(tamaños_celdas)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(tamaños_celdas)
                if evento.key == pygame.K_RETURN:
                    configuracion.cambiar_tamaño_celda(tamaños_celdas[seleccion])
                    return

def mostrar_seleccion_dificultad():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    niveles_dificultad = [5, 10, 15]
    seleccion = 1

    while True:
        pantalla.fill(configuracion.COLOR_FONDO)
        
        for i, nivel in enumerate(niveles_dificultad):
            color = configuracion.COLOR_TEXTO if i != seleccion else (255, 0, 0)
            texto = fuente.render(str(nivel), True, color)
            pantalla.blit(texto, (configuracion.ANCHO // 2 - 100, 100 + i * 50))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(niveles_dificultad)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(niveles_dificultad)
                if evento.key == pygame.K_RETURN:
                    configuracion.cambiar_velocidad_juego(niveles_dificultad[seleccion])
                    return

def mostrar_seleccion_sonido():
    pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
    fuente = configuracion.configurar_fuente()
    opciones_sonido = ["Encendido", "Apagado"]
    seleccion = 0

    while True:
        pantalla.fill(configuracion.COLOR_FONDO)
        
        for i, opcion in enumerate(opciones_sonido):
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
                    seleccion = (seleccion + 1) % len(opciones_sonido)
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones_sonido)
                if evento.key == pygame.K_RETURN:
                    configuracion.cambiar_estado_sonido(seleccion == 0)
                    if seleccion == 0:
                        sonidos.reproducir_musica_fondo()
                    else:
                        sonidos.detener_musica_fondo()
                    return
