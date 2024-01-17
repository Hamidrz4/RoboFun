import ctypes
import msvcrt
import os
import time
from datetime import date
from datetime import datetime

programmer_image_path = r"G:\Download\Browser\hi-tech-interface-abstract-9-4k.jpg"
researcher_image_path = r"G:\Download\Browser\super-abstract-digital-art-3840x2160_574954-mm-90.jpg"
student_image_path = r"G:\Download\Browser\mountain-landscape-abstract-4K-151.jpg"


def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def exit_program():
    print("No key pressed. Exiting.")
    exit()

today = date.today()
dyear = 365 - datetime.now().timetuple().tm_yday
dial=""

while True:
    print("Which ONE ??? (Programmer - Researcher - Student):\n ")
    input_str = ""
    start_time = time.time()

    while True:
        hour = time.strftime("%H:%M:%S", time.localtime())
        duration = time.time() - start_time
        if msvcrt.kbhit():
            input_char = msvcrt.getch().decode('utf-8')
            if input_char == " ":
                input_str += input_char
                start_time = time.time()
            else:
                break
        else:
            print(f"{dial}{duration} -> 10\n" * int(round(duration,2)*100))
            if duration > 10:
                exit_program()

    chosen_image_path = ""
    os.system("cls")

    if input_str == " ":
        chosen_image_path = programmer_image_path
        dial = f"You Are a Programmer | {today} | {dyear} | "
    elif input_str == "  ":
        chosen_image_path = researcher_image_path
        dial = f"You Are a Researcher | {today} | {dyear} | "
    elif input_str == "   ":
        chosen_image_path = student_image_path
        dial = f"You Are a Student | {today} | {dyear} | "
    else:
        print("Invalid input. Setting a neutral background.")
        continue

    set_wallpaper(chosen_image_path)

