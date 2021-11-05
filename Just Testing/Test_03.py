import pyglet
from pyglet.window import mouse
from pyglet.window import key

window = pyglet.window.Window(800,400, 'TRACKER')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
    elif button == mouse.RIGHT:
        print('The right mouse button was pressed.')
    elif button == mouse.MIDDLE:
        print('The middle mouse button was pressed.')

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button & mouse.LEFT:
        print("Draging with the left mouse button")
    elif button & mouse.RIGHT:
        print("Draging with the right mouse button")
    elif button & mouse.MIDDLE:
        print("Draging with the middle mouse button")

@window.event
def on_text_motion(motion):
    if motion == key.MOTION_UP:
        print('Moving up')
    elif motion == key.MOTION_DOWN:
        print('Moving down')
    elif motion == key.MOTION_RIGHT:
        print('Moving right')
    elif motion == key.MOTION_LEFT:
        print('Moving left')

@window.event
def on_draw():
    window.clear()

cursor = window.get_system_mouse_cursor(window.CURSOR_CROSSHAIR)
window.set_mouse_cursor(cursor)

pyglet.app.run()


#_______________________________

#*** Event logger ***

#event_logger = pyglet.window.event.WindowEventLogger()  
#window.push_handlers(event_logger)

#*** Event logger ***


#*** CHECKS keyboard buttons ***

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.BACKSPACE: # Symbolic names
#         print(f"{symbol} is equal to BACKSPACE button")

#     elif symbol == key.Z: #Alphabet keys
#         print(f"{symbol} is equal to 'Z' button")

#     elif symbol == key._1: # Number keypad keys
#         print("C")

#     elif symbol == key.NUM_1:  # Number keypad keys
#         print("D")

#*** CHECKS keyboard buttons ***

#_______________________________