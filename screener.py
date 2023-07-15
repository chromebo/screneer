import pytesseract
import keyboard
import mouse
import os
import clipboard
import sys
import pystray
from pyscreeze import screenshot
from winsound import Beep
from PIL import Image
from threading import Thread


def close():
    tray_icon.stop()
    exit()

def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)


def change_lang():
    global LANG
    if LANG == 'rus':
        LANG = 'eng'
    else:
        LANG = 'rus'


def main():
    while True:
        try:
            tray_icon.icon = green
            print('start')
            keyboard.wait('ctrl+q')
            tray_icon.icon = red
            Beep(1000, 100)
            print('combination')

            mouse.wait(button=mouse.LEFT, target_types=mouse.UP)
            first_click = mouse.get_position()
            print('first')
            mouse.wait(button=mouse.LEFT, target_types=mouse.UP)
            second_click = mouse.get_position()
            print('up')
            x_list = (first_click[0], second_click[0])
            y_list = (first_click[1], second_click[1])
            print(x_list)
            print(y_list)

            cords = (min(x_list), min(y_list), max(x_list) - min(x_list), max(y_list) - min(y_list))
            total_screen = screenshot(region=cords)
            total_screen.save(f'{os.getcwd()}\\temp.png')

            # image = Image.open(f'{os.getcwd()}\\temp.png')
            # image.show()

            text = pytesseract.image_to_string(f'{os.getcwd()}\\temp.png', lang=LANG)
            print(text)
            clipboard.copy(text)
            Beep(1500, 100)
        except:
            continue


if __name__ == '__main__':
    LANG = 'rus'
    green_file_path = resource_path('green.png')
    green = Image.open(green_file_path)
    red_file_path = resource_path('red.png')
    red = Image.open(red_file_path)
    tray_icon = pystray.Icon('Screener', green, menu=pystray.Menu(
        pystray.MenuItem('Смена языка', change_lang),
        pystray.MenuItem('Выход', close)
    ))

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract.exe'

    main_thread = Thread(target=main, daemon=True)
    main_thread.start()
    tray_icon.run()


