import pygame
import configuracion

class InterfazUsuario:
    def __init__(self, pantalla, fuente):
        self.pantalla = pantalla
        self.fuente = fuente

    def obtener_nombre_usuario(self):
        """Muestra una pantalla para obtener el nombre de usuario."""
        nombre = ""
        ingresando = True

        while ingresando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        ingresando = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += evento.unicode

            self.pantalla.fill(configuracion.COLOR_FONDO)
            mensaje = self.fuente.render("Ingrese su nombre de usuario:", True, configuracion.COLOR_TEXTO)
            self.pantalla.blit(mensaje, (configuracion.ANCHO // 2 - 150, configuracion.ALTO // 2 - 50))
            texto_nombre = self.fuente.render(nombre, True, configuracion.COLOR_TEXTO)
            self.pantalla.blit(texto_nombre, (configuracion.ANCHO // 2 - 150, configuracion.ALTO // 2))

            pygame.display.flip()

        return nombre

interfaz_usuario = InterfazUsuario
