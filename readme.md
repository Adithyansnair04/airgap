# Covert Channel Data Transmitters (Windows API)

A collection of Python proof-of-concept (PoC) scripts demonstrating out-of-band data transmission using low-level Windows API keyboard events.

## Overview

These scripts convert plain text payloads into 8-bit ASCII binary sequences and transmit the data bit-by-bit using simulated Virtual-Key events via native Windows binaries (`user32.dll`).

## Transmission Modules

This repository includes two distinct covert channel implementations:

### 1. Shift / Control Keypress Channel (`key_transmitter.py`)
Encodes binary data into continuous Virtual-Key press events:
* **Bit `1`**: Triggers a **Shift** key down/up event (`VK_SHIFT = 0x10`).
* **Bit `0`**: Triggers a **Ctrl** key down/up event (`VK_CONTROL = 0x11`).

### 2. CapsLock LED Visual Channel (`led_transmitter.py`)
Encodes binary data by manipulating the physical keyboard CapsLock indicator light:
* **Bit `1`**: Ensures CapsLock state is **ON** (toggles if OFF).
* **Bit `0`**: Ensures CapsLock state is **OFF** (toggles if ON).
* **State Optimization:** Key events are only triggered when transitioning between opposite bit states (e.g., `0` to `1`), leaving the CapsLock LED turned off once transmission finishes.

---

## Technical Comparison

| Feature | Shift / Ctrl Method | CapsLock LED Method |
| :--- | :--- | :--- |
| **Primary Channel** | Software Key Injection | Visual / Optical (LED) |
| **Physical Indicator** | None (Invisible on keyboard) | Keyboard CapsLock LED blinks |
| **Key Press Volume** | 1 keypress per bit | 1 keypress only on state changes |
| **Cleanup Action** | N/A | Automatically turns CapsLock OFF |

---

## Prerequisites

* **Operating System:** Windows only (Requires `os.name == 'nt'`)
* **Python Version:** Python 3.6+
* **Dependencies:** Built-in standard library (`time`, `ctypes`, `os`, `sys`)

---

## Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/covert-keyboard-channel.git](https://github.com/your-username/covert-keyboard-channel.git)
   cd covert-keyboard-channel
