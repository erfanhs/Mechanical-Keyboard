from pynput import keyboard
from playsound import playsound

current = set()

def on_press(key):
    if key in current: return
    else: current.add(key)
    
    if key == keyboard.Key.space:
        playsound('./audio/space.mp3', block=False)
    elif key == keyboard.Key.backspace:
        playsound('./audio/delete.mp3', block=False)
    else:
        playsound('./audio/key.mp3', block=False)


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

listner = keyboard.Listener(on_press=on_press, on_release=on_release)
listner.start()
listner.join()
