def mover_mono(mono, teclas):
    direccion = 0
    if teclas["left"]:
        direccion = -1
    elif teclas["right"]:
        direccion = 1
    mono.actualizar(direccion) 