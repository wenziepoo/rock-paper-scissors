items = ['A','B','C']
counter  = [0,0]
choice = ''
def on_gesture_shake():
    game()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
def on_button_pressed_a():
    counter = [0,0]
input.on_button_pressed(Button.A, on_button_pressed_a)

def game():
    global items
    radio.set_group(7)
    choice = items[randint(0,2)]
    radio.send_string(choice)
    score = str(counter[0]) + ' - ' + str(counter[1])

def on_received_string2(receivedString):
    pass
radio.on_received_string(on_received_string2)

def on_received_string(receivedString):
    global choice
    global counter
    def on_received_string2(receivedString):
        pass
    if choice == 'A':
        if receivedString == 'C':
            counter[1] = counter[1]+1
        elif receivedString != choice:
            counter[0] = counter[0]+1
    elif choice == 'B':
        if receivedString == 'A':
            counter[1] = counter[1]+1
        elif receivedString != choice:
                counter[0] = counter[0]+1
    elif choice == "C":
        if receivedString == 'B':
            counter[1] = counter[1]+1
        elif receivedString != choice:
            counter[0] = counter[0]+1
    radio.on_received_string(on_received_string)