# main.py
import time
import random
import subprocess
from coords import coords, deploy_locations
from config import BATTLE_LOOPS


def adb_tap(x, y):
    xj = int(x + random.randint(-6, 6))
    yj = int(y + random.randint(-6, 6))
    subprocess.run(['adb', 'shell', 'input', 'tap', str(xj), str(yj)])
    print(f"Tapped at: ({xj}, {yj})")


def deploy_troops():
    # Alternate between deploy locations, six pairs + one extra
    for _ in range(6):
        adb_tap(*coords['deploy'])
        adb_tap(*coords['deploy2'])
        adb_tap(*coords['deploy3'])
        adb_tap(*coords['deploy4'])
    adb_tap(*coords['deploy'])


def deploy_heroes():
    for hero in ['hero1', 'hero2', 'hero3', 'hero4']:
        adb_tap(*coords[hero])
        time.sleep(0.5)
        for deploy_point in deploy_locations:
            adb_tap(*coords[deploy_point])
            time.sleep(0.5)


def activate_all_heroes():
    for hero in ['hero1', 'hero2', 'hero3', 'hero4']:
        adb_tap(*coords[hero])


def run_battle():
    # Start matchmaking
    adb_tap(*coords['attack']);      time.sleep(4)
    adb_tap(*coords['find_match']); time.sleep(6)
    adb_tap(*coords['battle']);     time.sleep(3)
    adb_tap(*coords['select_troops']); time.sleep(2)

    # Deploy phase
    deploy_troops()
    deploy_heroes()

    # Hero activation burst
    time.sleep(2.5)
    activate_all_heroes()

    # Wait for battle to end, then surrender
    time.sleep(42)
    adb_tap(*coords['surrender']);     time.sleep(1)
    adb_tap(*coords['surrender_yes']); time.sleep(1)
    adb_tap(*coords['return_home']);   time.sleep(3)

if __name__ == "__main__":
    if BATTLE_LOOPS is None:
        loop = 1
        while True:
            run_battle()
            print(f"Battle {loop} complete — running forever")
            loop += 1
    else:
        for i in range(BATTLE_LOOPS):
            run_battle()
            remaining = BATTLE_LOOPS - (i + 1)
            print(f"Battle {i + 1}/{BATTLE_LOOPS} complete — {remaining} loop(s) remaining")