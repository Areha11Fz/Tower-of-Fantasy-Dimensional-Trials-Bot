import pyautogui as pt
import pydirectinput
import time
from win32gui import FindWindow, GetWindowRect, GetWindowText, GetForegroundWindow

lobbyPath = "images/lobby.png"
approvePath = "images/approve.png"
timerPath = "images/timer.png"

confidenceLevel = 0.7


def click(temp, x, y):
    pydirectinput.keyDown('alt')
    pt.moveTo(temp[0]+x, temp[1]+y)
    pydirectinput.click()
    pydirectinput.keyUp('alt')


def checkImage(path, rate):
    loc = pt.locateCenterOnScreen(path, confidence=rate)
    return loc


window = FindWindow(None, "Tower of Fantasy  ")

auto = True

while (True):
    if (GetWindowText(GetForegroundWindow()) != 'Tower of Fantasy  '):
        continue
    time.sleep(1)
    window_rect = GetWindowRect(window)

    inLobby = checkImage(lobbyPath, confidenceLevel)
    if (inLobby):
        auto = True
        # from open world click activities, select, dimensional trials
        # Adventure
        click(window_rect, 1140, 60)
        time.sleep(1)
        # Select
        click(window_rect, 150, 350)
        time.sleep(1)
        # Mid Dimen
        click(window_rect, 450, 450)
        time.sleep(1)
        # Go Right Corner
        click(window_rect, 1200, 700)
        time.sleep(1)
        # Go Activity
        click(window_rect, 900, 550)
        time.sleep(1)
        # Continue
        click(window_rect, 450, 450)
        time.sleep(1)
        # Match
        click(window_rect, 900, 450)
        time.sleep(1)

    inQueue = checkImage(approvePath, confidenceLevel)
    if (inQueue):
        time.sleep(1)
        click(window_rect, 800, 550)
        time.sleep(1)
        click(window_rect, 450, 450)
        time.sleep(1)

    inDomain = checkImage(timerPath, confidenceLevel)
    if (inDomain and auto):
        # auto battle
        time.sleep(1)
        click(window_rect, 800, 650)
        time.sleep(1)
        auto = False
