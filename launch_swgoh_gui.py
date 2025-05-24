#!/usr/bin/env python3

import pyautogui
import subprocess
import time
import os
import sys

# --- Settings ---
FOCUS_CLICK = (600, 100)
SWGOH_ICON = (575, 260)
BLUESTACKS_APP_NAME = "BlueStacks"

# --- Functions ---


   
def launch_bluestacks():
    """Launch Bluestacks using macOS 'open -a'."""
    try:
        subprocess.Popen(
            ["open", "-a", BLUESTACKS_APP_NAME],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("🚀 Launched Bluestacks.")
    except Exception as e:
        print(f"❌ Failed to launch Bluestacks: {e}")
        sys.exit(1)

def focus_window_mac(app_name):
    """Bring an app to the foreground using AppleScript."""
    print(f"⏳ Trying to focus window for: {app_name}")
    try:
        script = f'''
        tell application "System Events"
            if exists (process "{app_name}") then
                set frontmost of process "{app_name}" to true
                return "focused"
            else
                return "not found"
            end if
        end tell
        '''
        result = subprocess.check_output(['osascript', '-e', script]).decode().strip()
        if result == "focused":
            print("✅ Focused app window.")
            return True
        else:
            print("❌ App window not found.")
            return False
    except subprocess.CalledProcessError as e:
        print("❌ AppleScript error:", e)
        return False

def move_and_click(x, y):
    """Move the mouse to (x, y) and click."""
    print(f"🖱️ Moving to ({x}, {y}) and clicking...")
    pyautogui.moveTo(x, y)
    time.sleep(1.5)
    pyautogui.click()

def send_ctrl_shift_1():
    """Simulate pressing Ctrl + Shift + 1 to go Home in Bluestacks."""
    print("🎯 Sending Ctrl + Shift + 1 to go Home...")
    pyautogui.hotkey("ctrl", "shift", "1")
def home_esc():
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    pyautogui.hotkey("esc")
    time.sleep(0.5)
    move_and_click(*SWGOH_ICON)

def Galactic_War():
    print("🎯 Doing Galactic War...")
    pyautogui.hotkey("3")
    time.sleep(2)
    pyautogui.hotkey("H")
    time.sleep(2)
    pyautogui.hotkey("C")
    time.sleep(2)
    pyautogui.hotkey("D")
    time.sleep(2)
    pyautogui.hotkey("B")
    time.sleep(3)
    print("🎯 Done with Galactic War")
    home_esc()

def claim_rewards():
    print("🎯 Claiming rewards...")
    pyautogui.hotkey("1")
    time.sleep(2)
    pyautogui.hotkey("3")
    time.sleep(2)
    print("🎯 Done with claim rewards")
    home_esc()

def shipments():
    print("🎯 Doing shipments...")
    pyautogui.hotkey("3")
    time.sleep(2)
    pyautogui.hotkey("H")
    time.sleep(2)
    pyautogui.hotkey("1")
    time.sleep(2)
    pyautogui.hotkey("G")
    time.sleep(2)
    pyautogui.hotkey("B")
    time.sleep(2)
    pyautogui.hotkey("B")
    time.sleep(2)
    pyautogui.hotkey("B")
    time.sleep(2)
    pyautogui.hotkey("Y")
    time.sleep(2)
    pyautogui.hotkey("B")
    time.sleep(2)
    print("🎯 Done with shipments")
    home_esc()
    time.sleep(2)
    claim_rewards()

# --------- Main Run ---------
if __name__ == "__main__":
    # launch_bluestacks()
    #
    # print("⏳ Waiting 45 seconds for Bluestacks to load...")
    # time.sleep(45)
    #
    # # Try to focus Bluestacks up to 20 times (every 2 seconds)
    #
    # if not focused:
    #     print("❌ Could not focus Bluestacks after multiple attempts.")
    #     sys.exit(1)
    #
    # time.sleep(4)  # Let window stabilize
    #
    # move_and_click(*FOCUS_CLICK)      # First click to dismiss/focus
    # time.sleep(0.3)
    # move_and_click(*FOCUS_CLICK)      # First click to dismiss/focus
    # time.sleep(0.3)
    # move_and_click(*FOCUS_CLICK)      # First click to dismiss/focus
    # time.sleep(0.3)
    # move_and_click(*FOCUS_CLICK)      # First click to dismiss/focus
    # time.sleep(0.3)
    # move_and_click(*FOCUS_CLICK)      # First click to dismiss/focus
    #
    # time.sleep(3)
    #
    # send_ctrl_shift_1()               # Go Home
    # time.sleep(0.3)
    # send_ctrl_shift_1()               # Go Home
    # time.sleep(0.3)
    # send_ctrl_shift_1()               # Go Home
    # time.sleep(0.3)
    #
    # time.sleep(3)
    # move_and_click(*SWGOH_ICON)
    # time.sleep(0.3)
    # move_and_click(*SWGOH_ICON)         # Click SWGOH icon
    #
    # print("🎮 SWGOH should now be launching.")
    #
    # time.sleep(30)
    # Galactic_War()
    # shipments()

    #testing focus window
    focused = False
    for _ in range(20):
        if focus_window_mac(BLUESTACKS_APP_NAME):
            focused = True
            break
        time.sleep(2)
    time.sleep(3)



