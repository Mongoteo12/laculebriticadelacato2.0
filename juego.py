import pygame
import configuracion
from serpiente import serpiente
from manzana import manzana
from poder import poder
import sonidos
from logros import logros
from puntuaciones import puntuaciones
from estadisticas import estadisticas
from nivel import sistema_niveles

# Inicializamos pygame
pygame.init()

# Configuramos la pantalla
pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Configuramos la fuente
fuente = configuracion.configurar_fuente()

# Configuramos los sonidos
sonido_manzana, sonido_nivel, sonido_fin, sonido_error = configuracion.configurar_sonido()
configuracion.reproducir_musica_fondo()

# Función para mostrar mensaje en la pantalla
def mostrar_mensaje(pantalla, mensaje, color, posicion):
    texto = fuente.render(mensaje, True, color)
    pantalla.blit(texto, posicion)

# Pantalla de inicio del juego
def pantalla_inicio():
    pantalla.fill(configuracion.COLOR_FONDO)
    mostrar_mensaje(pantalla, "Juego de la Serpiente", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 100, configuracion.ALTO // 2 - 50))
    mostrar_mensaje(pantalla, "Presiona una tecla para iniciar", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 150, configuracion.ALTO // 2))

    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                esperando = False
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

# Pantalla de fin del juego
def pantalla_fin(puntuacion):
    pantalla.fill(configuracion.COLOR_FONDO)
    mostrar_mensaje(pantalla, "Fin del Juego", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 50, configuracion.ALTO // 2 - 50))
    mostrar_mensaje(pantalla, f"Puntuación: {puntuacion}", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 50, configuracion.ALTO // 2))
    mostrar_mensaje(pantalla, "Presiona una tecla para reiniciar", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 150, configuracion.ALTO // 2 + 50))

    configuracion.guardar_puntuacion(puntuacion)
    puntuaciones.mostrar_puntuaciones(pantalla, fuente)

    pygame.display.flip()
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN or evento.type == pygame.QUIT:
                esperando = False

# Pantalla de pausa
def pantalla_pausa():
    pantalla.fill(configuracion.COLOR_FONDO)
    mostrar_mensaje(pantalla, "Juego en Pausa", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 50, configuracion.ALTO // 2 - 50))
    mostrar_mensaje(pantalla, "Presiona P para continuar", configuracion.COLOR_TEXTO, (configuracion.ANCHO // 2 - 100, configuracion.ALTO // 2))

    pygame.display.flip()
    pausado = True
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = False
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

# Clase principal del juego para manejar todos los estados y lógica del juego
class Juego:
    def __init__(self):
        self.puntuacion = 0
        self.nivel = 0
        self.vidas = configuracion.VIDAS_INICIALES
        self.velocidad_temporal = False
        self.invencibilidad_temporal = False
        self.tiempo_efecto = 0

def bucle_juego(usuario):
    juego = Juego()
    reloj = pygame.time.Clock()
    serpiente.inicializar()
    manzana.generar_nueva()
    poder.generar_nueva()
    estadisticas.reiniciar()

    corriendo = True
    configuracion_nivel = sistema_niveles.obtener_nivel(juego.nivel)
    if configuracion_nivel is None:
        configuracion_nivel = sistema_niveles.niveles[-1]  # Utilizar el último nivel si no se encuentra un nivel válido
    juego_pausado = False
    tiempo_inicio = pygame.time.get_ticks()
    tiempo_notificacion = 0
    logro_mostrar = None

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
                configuracion.detener_musica_fondo()
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    juego_pausado = not juego_pausado
                    if juego_pausado:
                        pantalla_pausa()
                if evento.key == pygame.K_UP:
                    serpiente.cambiar_direccion((0, -configuracion.TAMAÑO_CELDA))
                if evento.key == pygame.K_DOWN:
                    serpiente.cambiar_direccion((0, configuracion.TAMAÑO_CELDA))
                if evento.key == pygame.K_LEFT:
                    serpiente.cambiar_direccion((-configuracion.TAMAÑO_CELDA, 0))
                if evento.key == pygame.K_RIGHT:
                    serpiente.cambiar_direccion((configuracion.TAMAÑO_CELDA, 0))

        if not juego_pausado:
            pantalla.fill(configuracion.COLOR_FONDO)
            try:
                serpiente.mover()
            except Exception as e:
                configuracion.reproducir_sonido(sonido_error)
                juego.vidas -= 1
                if juego.vidas == 0:
                    tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                    usuario.actualizar_estadisticas(juego.puntuacion, tiempo_total, juego.puntuacion // 10)
                    estadisticas.registrar_juego(juego.puntuacion, 0)
                    pantalla_fin(juego.puntuacion)
                    serpiente.inicializar()
                    manzana.generar_nueva()
                    poder.generar_nueva()
                    juego.puntuacion = 0
                    juego.nivel = 0
                    juego.vidas = configuracion.VIDAS_INICIALES
                    configuracion_nivel = sistema_niveles.obtener_nivel(juego.nivel)
                    estadisticas.reiniciar()
                else:
                    serpiente.inicializar()

            if serpiente.comer_manzana(manzana.posicion):
                juego.puntuacion += 10
                configuracion.reproducir_sonido(sonido_manzana)
                manzana.generar_nueva()
                estadisticas.actualizar_manzanas_comidas()
                estadisticas.actualizar_puntos_totales(10)
                nuevos_logros = logros.verificar_logros(juego.puntuacion, (pygame.time.get_ticks() - tiempo_inicio) // 1000, juego.nivel, juego.puntuacion // 10)
                if nuevos_logros:
                    for logro in nuevos_logros:
                        logro_mostrar = logro
                        tiempo_notificacion = pygame.time.get_ticks()
                if juego.puntuacion % 30 == 0:
                    juego.nivel += 1
                    configuracion_nivel = sistema_niveles.obtener_nivel(juego.nivel)
                    if configuracion_nivel is None:
                        configuracion_nivel = sistema_niveles.niveles[-1]  # Utilizar el último nivel si no se encuentra un nivel válido
                    configuracion.reproducir_sonido(sonido_nivel)
                    estadisticas.actualizar_niveles_completados()

            if serpiente.comer_poder(poder.posicion):
                poder.aplicar_efecto(juego)
                configuracion.reproducir_sonido(sonido_manzana)
                poder.generar_nueva()

            if serpiente.chocar_con_cuerpo():
                juego.vidas -= 1
                configuracion.reproducir_sonido(sonido_error)
                if juego.vidas == 0:
                    tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                    usuario.actualizar_estadisticas(juego.puntuacion, tiempo_total, juego.puntuacion // 10)
                    estadisticas.registrar_juego(juego.puntuacion, 0)
                    pantalla_fin(juego.puntuacion)
                    serpiente.inicializar()
                    manzana.generar_nueva()
                    poder.generar_nueva()
                    juego.puntuacion = 0
                    juego.nivel = 0
                    juego.vidas = configuracion.VIDAS_INICIALES
                    configuracion_nivel = sistema_niveles.obtener_nivel(juego.nivel)
                    estadisticas.reiniciar()

            serpiente.dibujar(pantalla)
            manzana.dibujar(pantalla)
            poder.dibujar(pantalla)

            texto_puntuacion = fuente.render(f"Puntuación: {juego.puntuacion}", True, configuracion.COLOR_TEXTO)
            pantalla.blit(texto_puntuacion, (10, 10))
            texto_nivel = fuente.render(f"Nivel: {juego.nivel}", True, configuracion.COLOR_TEXTO)
            pantalla.blit(texto_nivel, (10, 40))
            texto_vidas = fuente.render(f"Vidas: {juego.vidas}", True, configuracion.COLOR_TEXTO)
            pantalla.blit(texto_vidas, (10, 70))

            estadisticas.mostrar_estadisticas(pantalla, fuente)

            if logro_mostrar and (pygame.time.get_ticks() - tiempo_notificacion) < 3000:
                logros.mostrar_notificacion(pantalla, fuente, logro_mostrar)
            else:
                logro_mostrar = None

            if juego.velocidad_temporal and (pygame.time.get_ticks() - juego.tiempo_efecto) > 5000:
                juego.velocidad_temporal = False

            if juego.invencibilidad_temporal and (pygame.time.get_ticks() - juego.tiempo_efecto) > 5000:
                juego.invencibilidad_temporal = False

            pygame.display.flip()
            reloj.tick(configuracion_nivel['velocidad'] * (2 if juego.velocidad_temporal else 1))

    pygame.quit()
