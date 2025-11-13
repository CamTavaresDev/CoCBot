import time
import os
import random
import subprocess


coords = {
    'attack': (100, 800),
    'find_match': (364, 666),
    'select_troops': (170, 820),
    'deploy': (80, 424),
    'deploy2': (1540, 416),
    'surrender': (120, 670),
    'surrender_yes': (840, 535),
    'return_home': (800, 770),
}

def adb_tap(x, y):
    xj = int(x + random.randint(-6, 6))
    yj = int(y + random.randint(-6, 6))
    subprocess.run(['adb', 'shell', 'input', 'tap', str(int(xj)), str(int(yj))])
    print(f"Tapped at: ({int(xj)}, {int(yj)})")
    return x, y

if __name__ == "__main__":
    while True:
        adb_tap(*coords['attack'])
        time.sleep(1)
        adb_tap(*coords['find_match'])
        time.sleep(6)
        adb_tap(*coords['select_troops'])
        time.sleep(2)
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy'])
        time.sleep(35)
        adb_tap(*coords['surrender'])
        time.sleep(1)
        adb_tap(*coords['surrender_yes'])
        time.sleep(1)
        adb_tap(*coords['return_home'])
        time.sleep(3)

