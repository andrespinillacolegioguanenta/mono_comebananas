import os
import sys
import pygame

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from settings import ANCHO_PANTALLA, ALTO_PANTALLA, COLOR_FONDO, TIEMPO_NUEVA_BANANA
from MONO import Mono
from BANANA import Banana
from audiosjuego import AudioJuego
from movimiento import mover_mono


def reiniciar_juego():
    mono = Mono()
    bananas = []
    puntaje = 0
    contador = 0
    jugando = True
    return mono, bananas, puntaje, contador, jugando


def dibujar_texto(ventana, texto, x, y):
    fuente = pygame.font.SysFont("arial", 24)
    superficie = fuente.render(texto, True, (0, 0, 0))
    ventana.blit(superficie, (x, y))


def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption("Mono Banana")

    audio = AudioJuego()
    mono, bananas, puntaje, contador, jugando = reiniciar_juego()

    reloj = pygame.time.Clock()
    teclas = {"left": False, "right": False}

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    teclas["left"] = True
                elif evento.key == pygame.K_RIGHT:
                    teclas["right"] = True
                elif evento.key == pygame.K_r and not jugando:
                    mono, bananas, puntaje, contador, jugando = reiniciar_juego()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    teclas["left"] = False
                elif evento.key == pygame.K_RIGHT:
                    teclas["right"] = False

        if jugando:
            mover_mono(mono, teclas)
            contador += 1

            if contador >= TIEMPO_NUEVA_BANANA:
                bananas.append(Banana())
                contador = 0
                audio.reproducir_banana_aparece()

            for banana in bananas[:]:
                banana.actualizar()
                if banana.agarrada(mono.rect):
                    bananas.remove(banana)
                    puntaje += 1
                    audio.reproducir_banana_coja()
                elif banana.cayo():
                    jugando = False
                    audio.reproducir_perdio()
                    break

        ventana.fill(COLOR_FONDO)
        mono.dibujar(ventana)

        for banana in bananas:
            banana.dibujar(ventana)

        dibujar_texto(ventana, f"Puntaje: {puntaje}", 20, 20)
        dibujar_texto(ventana, f"Bananas atrapadas: {puntaje}", 20, 50)

        if not jugando:
            dibujar_texto(ventana, "Perdiste. Presiona R para reiniciar.", 200, 280)
            dibujar_texto(ventana, "Usa flechas izquierda/derecha para mover el mono.", 120, 320)

        pygame.display.flip()
        reloj.tick(60)


if __name__ == "__main__":
    main()