import pyautogui
import subprocess
import time
import psutil
import pygetwindow as gw

# Choose one of these
BLUESTACKS_PATH = r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"
SWGOH_PC_PATH = r"C:\Path\To\SWGOH_PC.exe"  # Replace with actual path

def launch_app(path):
    subprocess.Popen(path)
    print(f"Launched: {path}")

def wait_for_window(title_contains, timeout=60):
    print("Waiting for game window...")
    for _ in range(timeout):
        windows = gw.getWindowsWithTitle(title_contains)
        if windows:
            print("Game window found.")
            return windows[0]
        time.sleep(1)
    raise TimeoutError("Game window not found.")

def focus_and_click(window, x, y):
    window.activate()
    time.sleep(2)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(f"Clicked at ({x}, {y})")

# ---- Execution ----
if __name__ == "__main__":
    use_bluestacks = True  # Set to False for PC version

    exe_path = BLUESTACKS_PATH if use_bluestacks else SWGOH_PC_PATH
    launch_app(exe_path)

    # Adjust title string based on which game version you're using
    game_window = wait_for_window("Star Wars" if not use_bluestacks else "BlueStacks")

    # Click somewhere generic (top-right corner as an example)
    focus_and_click(game_window, 1000, 200)
