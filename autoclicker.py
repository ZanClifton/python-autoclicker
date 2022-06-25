import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

art = '''
                                            , ,
                                          ,','
                                         ; ;
                                         `.`.
                                           ) ;
                                      ,,,-','
                       _____,,,,---''",,,-'
             ___,,--'""_____,,,,--''""
     __,,--'"__,,--'"""
  ,-"_,,--'""
 ; ,'               .,------,....___
 ; ;               /       ;        """`---.._
 `.``-.._____,,,,,/       ;                   ""``.
   ``--...___;;;;/-"""""-;                         \\
             ```;        ;                         ;;
               ;        ;                         / ;
              ;"----....;___                     ; ;;
              ;-,,,,,___    ""`"--..._         ,' ; ;
              ;         """"``---...__""-...,-' ,'  ;
              ;                       "`-....,-'   /
              `-._     _-------_                 ,'
                  "`--'"""""""""``--..        ,,'
                                      ""`---'"
'''

print(art)
print("Welcome to the Auto Clicker!")
print("Use the 's' key to start and stop the autoclicker. Use 'e' to exit.")

delay = float(input(
    "How long would you like to wait between clicks in seconds? (1 is a single second, 10 is 10 seconds, 0.001 is 1 millisecond): "))
button = Button.left
start_stop_key = KeyCode(char="s")
exit_key = KeyCode(char="e")


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if not click_thread.running:
            click_thread.start_clicking()
        else:
            click_thread.stop_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
