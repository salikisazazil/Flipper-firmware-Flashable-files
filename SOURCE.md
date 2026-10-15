# WirelessPi Native Tools source

This folder contains two matching source components:

| Source | What it corresponds to |
| --- | --- |
| [WirelessPi-Native-Tools-1.0-source.tar.xz](WirelessPi-Native-Tools-1.0-source.tar.xz) | Complete original project for firmware `2.0.0-native-tools1` and the original apps, including cSploit Mini 1.0. |
| [RTL433-1.1.6-source.zip](RTL433-1.1.6-source.zip) | Complete updated RTL433 1.1.6 app source, vendored decoder library, UI, icon, licenses and host tests. This matches the newer RTL433 FAP in this repository. |

The original source ZIP has been losslessly repackaged as TAR.XZ to fit browser upload limits. Extract it with 7-Zip or `tar -xf WirelessPi-Native-Tools-1.0-source.tar.xz`. All source file contents are preserved. See `SOURCE-SHA256SUMS.txt` for download checksums.

It includes 6,059 files. The SDK, toolchain and generated build directories
are not bundled. Original component licenses and upstream notices remain
inside the source; this repository does not replace those licenses.

## Build the original firmware

1. Extract `WirelessPi-Native-Tools-1.0-source.tar.xz`; it creates
   `Flipper-Zero-ESP32-Port/`.
2. Install ESP-IDF **v5.4.1**, commit
   `4c2820d377d1375e787bcef612f0c32c1427d183`, with its submodules and ESP32-S3
   toolchain. Activate its environment (`export.sh` on Linux).
3. In that Python environment install `idf-component-manager==2.2.2` and
   Pillow. Preserve the project's dependency lockfile.
4. From the extracted project directory run:

```sh
bash BUILD-NATIVE-TOOLS.sh
```

This builds the firmware and original app versions using `sdkconfig.wifite`
and the `lilygo_t_embed_cc1101` target. The firmware output is
`build_native/furi_esp32.bin`. Existing SDK adapter steps are documented in
the extracted `BUILD-WIFITE.md`.

## Build the updated RTL433 1.1.6 FAP

The original archive predates RTL433 1.1.6. To produce the version supplied
in this repository, first complete the firmware build above, then replace
the extracted project's **entire** `applications_user/rtl433/` directory
with `applications_user/rtl433/` from the extracted `RTL433-1.1.6-source.zip`.

From the extracted firmware project, run:

```sh
FAP_FW_BUILD_DIR=build_native FAP_APP_VERSION_OVERRIDE=116 \
  bash buildFap.sh applications_user/rtl433
python3 tools/check_fap_symbols.py \
  components/flipper_application/flipper_application/firmware_api.c \
  build_native/fap/objects_rtl433.fap/undef_syms.txt
```

Install the resulting `build_native/fap/rtl433.fap` on the SD card at
`apps/Sub-GHz/rtl433.fap`. No new firmware flash is required for this app
update. If you run `BUILD-NATIVE-TOOLS.sh` again, rerun the RTL433 command
above afterward: the original helper uses the original app version override.

Host tests, with GCC and sanitizers available:

```sh
bash applications_user/rtl433/tests/run.sh
bash applications_user/csploit_mini/tests/run.sh
```

The packaged firmware and FAP binaries were matched to the corresponding
release artifacts before adding these sources. Rebuilding is not promised
to produce byte-identical binaries across different toolchains, paths and
build timestamps. Firmware images are unchanged by this source upload.
