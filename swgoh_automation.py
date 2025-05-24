#!/usr/bin/env python3

import pyautogui
import subprocess
import time
import os

def launch_bluestacks():
    """Launch Bluestacks using macOS 'open -a'."""
    try:
        subprocess.Popen(
            ["open", "-a", "BlueStacks"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("🚀 Launched Bluestacks.")
    except Exception as e:
        print(f"❌ Failed to launch Bluestacks: {e}")
        exit(1)

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
    pyautogui.click()

# --------- Main Run ---------
if __name__ == "__main__":
    launch_bluestacks()

    # Try to focus Bluestacks up to 20 times (every 2 seconds)
    focused = False
    for _ in range(20):
        if focus_window_mac("BlueStacks"):
            focused = True
            break
        time.sleep(2)

    if not focused:
        print("❌ Could not focus Bluestacks after multiple attempts.")
        exit(1)

    time.sleep(2)  # Let window stabilize

    # Test click (adjust this coordinate as needed)
    move_and_click(800, 200)
