# WirelessPi Native Tools 1.0 — T-Embed firmware and source

Firmware **2.0.0-native-tools1** for the **LilyGo T-Embed CC1101 / CC1101 Plus
(ESP32-S3, 16 MiB flash)**, based on the Sor3nt ESP32 port.
WirelessPi is the build name; no Raspberry Pi is required.

- **[Flash with Spacehuhn ESPWebTool](FLASHING.md)** — step-by-step browser instructions and verified addresses.
- **[Firmware and SD apps](Flipper%20zero%20T-embed-Native-Tools-1.0/)** — four firmware images plus WIFITE, RTL433, Wardriver, WDGWars Map, BW16 I2C, ProtoPirate 3.6.3 and cSploit Mini.
- **[Source and build instructions](SOURCE.md)** — complete original firmware source and separate all-app source ZIP.
- **[Checksums](Flipper%20zero%20T-embed-Native-Tools-1.0/SHA256SUMS.txt)** and **[release manifest](Flipper%20zero%20T-embed-Native-Tools-1.0/release-manifest.json)**.

Download this repository using **Code → Download ZIP**, then extract it.
The firmware files are inside `Flipper zero T-embed-Native-Tools-1.0/firmware/`.

| Firmware file | Flash address |
| --- | --- |
| `bootloader.bin` | `0x0000` |
| `partition-table.bin` | `0x8000` |
| `furi_esp32.bin` | `0x10000` |
| `ota_data_initial.bin` | `0xBF0000` |

These addresses belong to this build. Set them manually in the web flasher.
The full instructions also cover download mode and installing SD apps.

If WirelessPi Native Tools 1.0 is already installed and you only want the
RTL433 update, replace `apps/Sub-GHz/rtl433.fap` on the SD card. A firmware
reflash is not needed for that update.

The firmware binaries are unchanged. RTL433 1.1.6 is a separate app update;
its current source and validation logs are included in the RTL433 source ZIP. See the release README
for feature scope and hardware-validation limits. These are ESP32-port files,
not firmware for a stock Flipper Zero. Original source licenses and notices
remain with their respective components.

## ProtoPirate asset correction

The SD package now includes `apps_assets/proto_pirate/keystore/` and `models_db/`, previously omitted, alongside all 34 matching `pp_*.fal` plugins. These three data files match the existing published source archive byte for byte. Firmware and FAP binaries are unchanged. This corrects packaging; it is not a confirmed fix for every reported menu failure.

Copy both `apps/` and `apps_assets/` to the SD card root. Use `apps/Sub-GHz/proto_pirate.fap` from this release. If your card also has `apps/SubGhz/proto_pirate.fap`, back up that older copy outside the apps folder to avoid launching the wrong app. Legacy `protopirate_*_plugin.fal` files are not required by this release; use the supplied `pp_*.fal` set. Preserve your captures and settings.

The uploaded working-card archive contained duplicate ProtoPirate versions and older plugins; those duplicates were not added to this clean release. Both the main FAP and all 34 plugins were checked: 324 unique firmware imports, zero missing exports in the packaged firmware. Runtime behavior on affected devices remains unverified.
