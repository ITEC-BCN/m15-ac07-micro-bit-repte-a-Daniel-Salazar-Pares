def mostrar_piedra():
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    """)

def mostrar_papel():
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
    """)

def mostrar_tijeras():
    basic.show_leds("""
        # # . . #
        . # # . .
        . . # . .
        . # # . .
        # # . . #
    """)

eleccion_maquina = -1

def on_gesture_shake():
    global eleccion_maquina
    eleccion_maquina = randint(0, 2)  # 0: piedra, 1: papel, 2: tijeras
    if eleccion_maquina == 0:
        mostrar_piedra()
    elif eleccion_maquina == 1:
        mostrar_papel()
    else:
        mostrar_tijeras()

def determinar_ganador(eleccion_jugador):
    global eleccion_maquina
    if eleccion_jugador == eleccion_maquina:
        basic.show_string(" EMPATE")
    elif (eleccion_jugador == 0 and eleccion_maquina == 2) or \
         (eleccion_jugador == 1 and eleccion_maquina == 0) or \
         (eleccion_jugador == 2 and eleccion_maquina == 1):
        basic.show_string(" GANAS!")
    else:
        basic.show_string(" PIERDES")

def on_button_a_pressed():
    mostrar_piedra()
    determinar_ganador(0)  # 0 representa piedra

def on_button_b_pressed():
    mostrar_papel()
    determinar_ganador(1)  # 1 representa papel

def on_buttons_ab_pressed():
    mostrar_tijeras()
    determinar_ganador(2)  # 2 representa tijeras

input.on_button_pressed(Button.A, on_button_a_pressed)
input.on_button_pressed(Button.B, on_button_b_pressed)
input.on_button_pressed(Button.AB, on_buttons_ab_pressed)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
