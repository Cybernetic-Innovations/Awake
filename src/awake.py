import argparse
import json
import os
import pyautogui
import random
import sys
import time
from loguru import logger

FILE_PATH = os.path.dirname(__file__)
logger.configure(**{"handlers": [{"sink": sys.stdout, "format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <cyan><level>{message}</level></cyan>"}]})

pyautogui.FAILSAFE = False

lastMouse = pyautogui.position()

parser = argparse.ArgumentParser(description='Keep your pc awake while your away')
parser.add_argument('-m', dest='minutes', type=int, default=1, help="Time between activity check, default=3")
parser.add_argument('-k', dest='key', type=str, default='None', help="Key to press, default=None")
args = parser.parse_args()


def loadQuotes():
    file_path = os.path.join(FILE_PATH, "quotes.json")
    with open(file_path) as f:
        oJson = json.load(f)
    return oJson['quotes']


def move(curPosition):
    positionX = [random.randrange(-10, 10, 1) for _ in range(5)]
    positionY = [random.randrange(-10, 10, 1) for _ in range(5)]

    for i in range(0, len(positionX)):
        pyautogui.moveTo(curPosition.x + positionX[i], curPosition.y + positionY[i])

    oKey = args.key.split(':')
    if len(oKey) == 2:
        for i in range(0, int(oKey[1])):
            pyautogui.press(oKey[0])

    pyautogui.moveTo(curPosition.x, curPosition.y)


if __name__ == '__main__':
    if args.key == 'None':
        logger.debug(f'Welcome to Awake, I will check every {args.minutes} min/s to see if there is any activity. If no activity will move the mouse.')
    else:
        arg = args.key.split(":")
        logger.debug(f'Welcome to Awake, I will check every {args.minutes} min/s to see if there is any activity. If no activity will move the mouse and press `{arg[0]}` {arg[1]} times.')

    quotes = loadQuotes()

    while True:
        time.sleep(60 * args.minutes)
        curMouse = pyautogui.position()

        q = random.randrange(len(quotes))
        if lastMouse == curMouse:
            logger.warning(f'{quotes[q]["quote"]}')
            move(curMouse)
        else:
            logger.info(f'{quotes[q]["quote"]}')

        lastMouse = curMouse
