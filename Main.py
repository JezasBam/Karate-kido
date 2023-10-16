import pyautogui
import cv2
import numpy as np
import time

while True:
    # facem un screenshot doar pe porțiunea specificată
    screenshot = pyautogui.screenshot(region=(500, 600, 600, 300))

    # convertim screenshot-ul într-un array numpy
    screenshot = np.array(screenshot)

    # convertim culorile din BGR în RGB
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

    # afișăm screenshot-ul într-o fereastră separată
    cv2.imshow('Screenshot', screenshot)

    # așteptăm 1 secundă înainte de a face următorul screenshot
    time.sleep(0.01)

    # verificăm dacă utilizatorul a apăsat tasta 'q' pentru a închide fereastra
    if cv2.waitKey(1) == ord('q'):
        break

# închidem fereastra
cv2.destroyAllWindows()