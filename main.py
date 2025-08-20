count = 0

def on_button_pressed_a():
    global count
    count = 1
    basic.show_number(count)

def on_button_pressed_b():
    global count
    count = 2
    basic.show_number(count)

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
