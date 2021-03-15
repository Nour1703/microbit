input.onButtonPressed(Button.AB, function () {
    basic.showString("Start")
    if (input.buttonIsPressed(Button.A)) {
        basic.showIcon(IconNames.Heart)
        basic.showString("big heart")
    } else {
        basic.showIcon(IconNames.SmallHeart)
        basic.showString("small heart")
    }
})
