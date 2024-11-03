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

def on_button_a_pressed():
    mostrar_piedra()

def on_button_b_pressed():
    mostrar_papel()

def on_buttons_ab_pressed():
    mostrar_tijeras()

def on_gesture_shake():
    eleccion = randint(0, 3)
    if eleccion == 0:
        mostrar_piedra()
    elif eleccion == 1:
        mostrar_papel()
    else:
        mostrar_tijeras()

input.on_button_pressed(Button.A, on_button_a_pressed)
input.on_button_pressed(Button.B, on_button_b_pressed)
input.on_button_pressed(Button.AB, on_buttons_ab_pressed)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
