# Flashing the T-Embed ESP32-S3

**For Spacehuhn browser flashing, use [the step-by-step guide](../FLASHING.md).**
The commands below are an alternative Python flashing method.

Use these images only for the T-Embed CC1101 / CC1101 Plus configuration with
16 MiB flash used by this WirelessPi build. They are not Flipper Zero images.
RTL433 alone can use the previous firmware; the new cSploit Mini packet/TCP
API needs this firmware update.

Keep a copy of your current firmware and SD files. Merge `SD/` onto the SD
card separately; flashing the ESP32 does not install these FAP files.

1. Install Python and `esptool==4.12.0`:
   `python -m pip install esptool==4.12.0`
2. Connect the T-Embed over USB and identify its serial port.
3. From this extracted release folder, verify the image hashes:
   `python flash.py --verify-only`
4. Flash, replacing the example port with yours:
   `python flash.py --port COM5`
   or `python3 flash.py --port /dev/ttyACM0`

The helper uses ESP32-S3, DIO, 80 MHz, 16 MiB flash and these offsets from the
build's generated flash arguments:

| Offset | Image |
| --- | --- |
| `0x0` | `firmware/bootloader.bin` |
| `0x8000` | `firmware/partition-table.bin` |
| `0x10000` | `firmware/furi_esp32.bin` |
| `0xbf0000` | `firmware/ota_data_initial.bin` |

The script verifies hashes before invoking esptool. It writes the listed
regions and resets OTA selection to the packaged application; it does not
issue a full-flash erase. If automatic download mode fails, use your board's
BOOT/RESET procedure. No flashing or physical-device verification was
performed during this build.
