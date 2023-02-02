let items = ["A", "B", "C"]
let counter = [0, 0]
let choice = ""
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    game()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let counter = [0, 0]
})
function game() {
    
    radio.setGroup(7)
    let choice = items[randint(0, 2)]
    radio.sendString(choice)
    let score = "" + counter[0] + " - " + ("" + counter[1])
}

radio.onReceivedString(function on_received_string2(receivedString: string) {
    
})
