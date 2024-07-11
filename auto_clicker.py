import subprocess
import time
import random

def adb_click(x_range, y_range):
    x = random.randint(x_range[0], x_range[1])
    y = random.randint(y_range[0], y_range[1])
    adb_command = f'adb -s Z5KNAIWKDA798TNJ shell input tap {x} {y}'
    subprocess.run(adb_command, shell=True)

while True:
    adb_click((350, 370), (1150, 1250))
    time.sleep(3)
