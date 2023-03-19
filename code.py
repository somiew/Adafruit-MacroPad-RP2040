import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_macropad import MacroPad

macropad = MacroPad()
macropad_layer = 0
prev_enc = 0

# Main Group
main_group = displayio.Group()
# macropad.display.show(main_group) # for now to test the encoder
title = label.Label(
    y=4,
    font=terminalio.FONT,
    color=0x0,
    text="       MACROSAM       ",
    background_color=0xFFFFFF,
)
layout = GridLayout(x=0, y=10, width=128, height=54, grid_size=(3, 4), cell_padding=1)
labels = []
numpadLabels = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", ",", "enter"]

for each in numpadLabels:
    labels.append(label.Label(terminalio.FONT, text=each))

for index in range(12):
    x = index % 3
    y = index // 3
    layout.add_content(labels[index], grid_position=(x, y), cell_size=(1, 1))

main_group.append(title)
main_group.append(layout)

# Nuke Group
nuke_group = displayio.Group()
title = label.Label(
    y=4,
    font=terminalio.FONT,
    color=0x0,
    text="         NUKE         ",
    background_color=0xFFFFFF,
)

layout = GridLayout(x=0, y=10, width=128, height=54, grid_size=(3, 4), cell_padding=1)
labels = []
numpadLabels = ["Save 1", "Save 2", "Save 3", "Go 1", "Go 2", "Go 3", "1", "2", "3", "0", ",", "enter"]

for each in numpadLabels:
    labels.append(label.Label(terminalio.FONT, text=each))

for index in range(12):
    x = index % 3
    y = index // 3
    layout.add_content(labels[index], grid_position=(x, y), cell_size=(1, 1))

nuke_group.append(title)
nuke_group.append(layout)

# macropad.display_image("jasmine.bmp")

while True:
    key_event = macropad.keys.events.get()

    if macropad_layer == 0:

        macropad.display.show(main_group)

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_SEVEN)
                if key_event.key_number == 1:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_EIGHT)
                if key_event.key_number == 2:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_NINE)

                if key_event.key_number == 3:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_FOUR)
                if key_event.key_number == 4:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_FIVE)
                if key_event.key_number == 5:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_SIX)

                if key_event.key_number == 6:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ONE)
                if key_event.key_number == 7:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_TWO)
                if key_event.key_number == 8:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_THREE)

                if key_event.key_number == 9:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ZERO)
                if key_event.key_number == 10:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_PERIOD)
                if key_event.key_number == 11:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ENTER)
                    macropad.display_image("jasmine.bmp")

    if macropad_layer == 1:

        macropad.display.show(nuke_group)

        if key_event:
            if key_event.pressed:
                if key_event.key_number == 0:
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.F7)
                if key_event.key_number == 1:
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.F8)
                if key_event.key_number == 2:
                    macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.F9)

                if key_event.key_number == 3:
                    macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.F7)
                if key_event.key_number == 4:
                    macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.F8)
                if key_event.key_number == 5:
                    macropad.keyboard.send(macropad.Keycode.SHIFT, macropad.Keycode.F9)

                if key_event.key_number == 6:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ONE)
                if key_event.key_number == 7:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_TWO)
                if key_event.key_number == 8:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_THREE)

                if key_event.key_number == 9:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ZERO)
                if key_event.key_number == 10:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_PERIOD)
                if key_event.key_number == 11:
                    macropad.keyboard.send(macropad.Keycode.KEYPAD_ENTER)

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.mouse.click(macropad.Mouse.RIGHT_BUTTON)
        print(
        "enc_" + str(macropad.encoder) +
        " mp_" + str(macropad_layer) +
        " pe_" + str(prev_enc)
        )

    if macropad.encoder > prev_enc:
        macropad_layer = 1
        prev_enc = macropad.encoder
        print(macropad_layer)

    if macropad.encoder < prev_enc:
        macropad_layer = 0
        prev_enc = macropad.encoder
        print(macropad_layer)
