def on_button_pressed_ab():
    basic.show_string("Start")
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HEART)
        basic.show_string("big heart")
    else:
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_string("small heart")
input.on_button_pressed(Button.AB, on_button_pressed_ab)
