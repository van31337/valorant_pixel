import cv2
import numpy as np
import threading
import time
import win32api

from screen_cap import ScreenCapture
from mouse import SocketArduinoMouse


LOWER_COLOR = np.array([140, 110, 150])
UPPER_COLOR = np.array([150, 195, 255])
THRESHOLD = 60

class runner:
    def __init__(self, x, y, grabzone):
        self.arduinomouse = SocketArduinoMouse()
        self.grabber = ScreenCapture(x, y, grabzone)
        threading.Thread(target=self.run, daemon=True).start()
        self.toggled = False

    def toggle(self):
        self.toggled = not self.toggled
        time.sleep(0.2)

    def run(self):
        while True:
            if win32api.GetKeyState(0x01) < 0 and self.toggled:
                self.process("move")
            elif win32api.GetKeyState(0x05) < 0 and self.toggled:
                self.process("click")

    def process(self, action):
        screen = self.grabber.get_screen()
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
        dilated = cv2.dilate(mask, None, iterations=5)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if not contours:
            return

        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        center = (x + w // 2, y + h // 2)

        if action == "move":
            cX = x + w // 2
            cY = y + 9
            x_diff = cX - self.grabber.grabzone // 2
            y_diff = cY - self.grabber.grabzone // 2
            self.arduinomouse.sendMouseCoordinates(x_diff * 0.3, y_diff * 0.3)

    def close(self):
        if hasattr(self, 'arduinomouse'):
            # Cleanup code for SocketArduinoMouse
            pass
        self.toggled = False

    def __del__(self):
        self.close()