function mostrar_piedra() {
    basic.showLeds(`
        . . . . . 
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    `)
}

function mostrar_papel() {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
    `)
}

function mostrar_tijeras() {
    basic.showLeds(`
        # # . . #
        . # # . .
        . . # . .
        . # # . .
        # # . . #
    `)
}

input.onButtonPressed(Button.A, function on_button_a_pressed() {
    mostrar_piedra()
})
input.onButtonPressed(Button.B, function on_button_b_pressed() {
    mostrar_papel()
})
input.onButtonPressed(Button.AB, function on_buttons_ab_pressed() {
    mostrar_tijeras()
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let eleccion = randint(0, 3)
    if (eleccion == 0) {
        mostrar_piedra()
    } else if (eleccion == 1) {
        mostrar_papel()
    } else {
        mostrar_tijeras()
    }
    
})
