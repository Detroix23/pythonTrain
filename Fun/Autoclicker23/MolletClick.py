from pynput import Controller
mouse = Controller()

def on_scroll(x, y, dx, dy):
    mouse.click(Button.right, 1)

while 1:
    on_scroll()