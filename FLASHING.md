# Flash WirelessPi Native Tools 1.0 with Spacehuhn ESPWebTool

This guide installs **WirelessPi Native Tools 1.0**, firmware
**2.0.0-native-tools1**, on the **LilyGo T-Embed CC1101 / CC1101 Plus
(ESP32-S3, 16 MiB flash)**. WirelessPi is the firmware's name; no Raspberry Pi
is involved. These images are not for a stock Flipper Zero or other ESP boards.

## 1. Download the files

1. Open [this repository](https://github.com/salikisazazil/Flipper-firmware-Flashable-files).
2. Select **Code → Download ZIP**, then extract the ZIP on your computer.
3. Open `Flipper zero T-embed-Native-Tools-1.0/firmware/` in the extracted folder.
4. Locate `bootloader.bin`, `partition-table.bin`, `furi_esp32.bin`, and
   `ota_data_initial.bin`. You will select all four files in the flasher.

Keep a backup of your existing SD files and any internal settings you need.
You do not upload the repository ZIP, source ZIP or `.fap` files to the web flasher.

## 2. Connect the T-Embed

1. Use desktop **Chrome or Microsoft Edge** and a USB cable that supports data.
2. Close serial monitors, other flashers and other browser tabs using the device.
3. Connect the T-Embed directly to the computer.
4. Open **[esptool.spacehuhn.com](https://esptool.spacehuhn.com/)**.
5. Use **115200 baud** for the initial attempt. If you change Settings, save
   before connecting. Higher speeds such as 460800/921600 are optional;
   return to 115200 if a transfer fails.
6. Click **Connect**, choose the T-Embed's USB serial port, and connect.
   Confirm the detected chip is **ESP32-S3** before programming.

If it cannot connect, enter download mode manually: hold the button in the
middle of the rotary encoder (**BOOT**), press and release **RST** on the
back, then release BOOT. Reconnect in the browser; the COM port may change.
The display may remain blank in download mode.

## 3. Select all four files and set their addresses

Use **Select** for each file and **Add** if another row is needed. Replace
any saved files/addresses from an earlier flashing session.

| Select this file from `firmware/` | Address | Type into the field labelled `0x` |
| --- | --- | --- |
| `bootloader.bin` | `0x0000` | `0` |
| `partition-table.bin` | `0x8000` | `8000` |
| `furi_esp32.bin` | `0x10000` | `10000` |
| `ota_data_initial.bin` | `0xBF0000` | `BF0000` |

**Use these exact file/address pairs.** The flasher's generic ESP32 defaults
can show `1000` and `E000`; those are not the bootloader/OTA addresses for
this ESP32-S3 build. Its bootloader starts at `0`, and its OTA data is at
`BF0000`. The address boxes already have a `0x` label, so enter only the
hexadecimal digits shown in the last column.

The release was built for **DIO / 80 MHz / 16 MiB**. Spacehuhn's UI normally
only exposes the baud setting; the supplied binaries contain their image
headers. No Arduino board settings or recompilation are needed.

## 4. Program and restart

1. Check all four filenames and addresses again.
2. Click **Program** and accept its confirmation.
3. Leave the cable connected until all four files finish. Check the output
   for errors for every file; do not rely on a single progress percentage.
4. Disconnect the browser's serial connection and press **RST** once with
   BOOT released. If necessary, reconnect USB.
5. Let the firmware start. The included firmware revision is
   **2.0.0-native-tools1**.

A separate full-chip **Erase** is not required for this procedure. It removes
internal settings and other flash contents. Programming these four files
writes the packaged regions and resets OTA selection to the packaged app.

## 5. Install the apps on the SD card

Firmware flashing does not copy `.fap` apps to the SD card.

1. Close any running apps and access the SD card using a card reader or the
   firmware's supported file-transfer method.
2. Copy the **contents** of `Flipper zero T-embed-Native-Tools-1.0/SD/` to
   the **root** of the SD card, merging folders and preserving unrelated data.
3. The resulting paths must be:
   - `apps/Sub-GHz/rtl433.fap` — **RTL433 1.1.6**
   - `apps/WiFi/csploit_mini.fap` — **cSploit Mini 1.0**
4. Safely eject/reinsert the card as appropriate and open the apps from the
   firmware's application browser.

Do not create an extra `SD` directory on the card. If Native Tools 1.0 is
already installed, updating RTL433 only requires replacing its `.fap`;
you can skip the firmware flashing steps.

## Troubleshooting

- **No serial port:** try another data cable/USB port, close other serial
  programs and enter BOOT/RST download mode.
- **Connection or write timeout:** reconnect at 115200 baud and retry.
- **Firmware will not start:** make sure BOOT is released, restart, and
  recheck all four address/file pairs, especially `0` and `BF0000`.
- **App missing:** check its SD path; `.fap` files are not flash images.
- **Need to verify downloads:** from the release folder, run
  `python flash.py --verify-only` to verify the four firmware images without
  connecting to or flashing the device. `SHA256SUMS.txt` covers the release
  files, including source and apps.

## Sources for these instructions

- [This build's release manifest](Flipper%20zero%20T-embed-Native-Tools-1.0/release-manifest.json)
- [Original partition layout and build source](SOURCE.md)
- [Spacehuhn's browser flashing guide](https://docs.spacehuhn.com/blog/espwebtool/)
- [Spacehuhn address/file UI](https://github.com/SpacehuhnTech/espwebtool/blob/main/src/components/FileList.js)
- [LilyGo T-Embed CC1101 download-mode procedure](https://github.com/Xinyuan-LilyGO/T-Embed-CC1101/blob/master/docs/download_mode.md)

The address map and binary hashes have been checked against the release.
This documentation update did not physically flash or test a T-Embed.
