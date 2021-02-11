import keyboard
import pyperclip

keyboard.add_hotkey('num lock', lambda:keyboard.write("".join(pyperclip.paste().split("\n")).replace('\t', ''), 0.1, 0))
keyboard.wait('esc')
