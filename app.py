import time
import ctypes
import os
import sys

# Virtual-Key codes for visible keys
VK_SHIFT = 0x10  # Shift key
VK_CONTROL = 0x11  # Ctrl key

# Ensure the script runs only on Windows
if os.name != 'nt':
    print("[-] This script only works on Windows.")
    sys.exit(1)


def press_key(vk_code):
    ctypes.windll.user32.keybd_event(vk_code, 0, 0, 0)   # Key down
    time.sleep(0.05)
    ctypes.windll.user32.keybd_event(vk_code, 0, 2, 0)   # Key up


def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)


def blink_keys(bits, delay=0.3):
    print(f"[*] Transmitting bits: {bits}")
    for bit in bits:
        print(f"[>] Bit: {bit}")
        if bit == '1':
            press_key(VK_SHIFT)
        else:
            press_key(VK_CONTROL)
        time.sleep(delay)
    print("[+] Transmission complete.")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    message = "ADITHYAN"
    print(f"[+] Encoding message: {message}")
    bits = text_to_bits(message)
    blink_keys(bits)


if __name__ == "__main__":
    main()
