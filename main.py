import os
import time
import keyboard
from termcolor import colored
from runner import runner

TOGGLE_KEY = 'F1'
FOV = 50
CENTER_X, CENTER_Y = 1920 // 2, 1080 // 2

def main():
    os.system('not valorant aimbot')
    shyne1337_obj = runner(CENTER_X - FOV // 2, CENTER_Y - FOV // 2, FOV)
    print()
    print(colored('[Info]', 'blue'), colored('Set enemies to', 'white'), colored('Purple', 'yellow'))
    print(colored('[Info]', 'blue'), colored(f'Press {TOGGLE_KEY} to toggle ON/OFF', 'white'))
    print(colored('[Info]', 'blue'), colored('Default settings are', 'white'),
          colored('LeftMB', 'yellow'), colored('= Aimbot,', 'white'),
          colored('Mouse5', 'yellow'), colored('= Triggerbot', 'white'))
    print(colored('[Info]', 'blue'), colored('Made By', 'white'), colored('sHyNe1337', 'yellow'))
    status = 'Disabled'

    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                shyne1337_obj.toggle()
                status = 'Enabled ' if shyne1337_obj.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "blue")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'blue'), colored('Exiting...', 'white') + '\n')
    finally:
        shyne1337_obj.close()

if __name__ == '__main__':
    main()
