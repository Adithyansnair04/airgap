import time
import ctypes
import os
import sys

# Virtual-Key codes
VK_CAPITAL = 0x14           # CapsLock

if os.name != 'nt':
    print("[-] This script only works on Windows.")
    sys.exit(1)

# Toggle key using keybd_event


def toggle_key(vk_code):
    ctypes.windll.user32.keybd_event(vk_code, 0, 0, 0)
    ctypes.windll.user32.keybd_event(vk_code, 0, 2, 0)

# Check CapsLock state


def is_caps_on():
    return ctypes.windll.user32.GetKeyState(VK_CAPITAL) & 0x0001

# Toggle CapsLock LED


def toggle_capslock():
    toggle_key(VK_CAPITAL)

# Encode message to bits


def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Transmit using LED and mute toggle


def blink_capslock_and_mute(bits, delay=0.5):
    print(f"[*] Transmitting bits: {bits}")
    for bit in bits:
        print(f"[>] Bit: {bit}")
        if bit == '1':
            if not is_caps_on():
                toggle_capslock()
        else:
            if is_caps_on():
                toggle_capslock()
        time.sleep(delay)

    # Ensure LED is off after transmission
    if is_caps_on():
        toggle_capslock()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    message = "ADITHYAN"
    print(f"[+] Encoding message: {message}")
    bits = text_to_bits(message)
    blink_capslock_and_mute(bits)
    print("[+] Transmission complete.")


if __name__ == "__main__":
    main()
