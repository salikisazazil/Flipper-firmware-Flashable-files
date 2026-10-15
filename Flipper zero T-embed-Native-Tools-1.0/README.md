# WirelessPi Native Tools 1.0

Two native ESP32-S3 apps for the LilyGo T-Embed CC1101 / CC1101 Plus running
the Sor3nt-based WirelessPi port. No Raspberry Pi is involved. These FAPs are
for this ESP32 port, not stock Flipper Zero firmware.

## Included

- **RTL433 1.0:** CC1101 OOK/FSK receiver and rtl_433 decoder adaptation,
  selectable decoders, history, full JSON details, SD logs/exports, raw-pulse
  save/load and offline decoding. See `docs/RTL433.md` for radio limitations.
- **cSploit Mini 1.0:** native LAN/TCP diagnostics, DNS/HTTP inspection,
  TCP/UDP text requests, one-target ARP relay, exact-name DNS redirect,
  LLMNR/NBT-NS responses and an HTTP exposure indicator. See
  `docs/cSploit-Mini.md` for the exact scope and configuration.
- Compact font and launcher icons for both apps.
- Firmware `2.0.0-native-tools1`, flash helper, complete project source and
  build/test logs.

These are selected native implementations, not complete desktop rtl_433 or
Android cSploit/dSploit ports. The exposure indicator records connection and
Authorization-header presence only; it discards values and does not collect
passwords, session tokens or authentication hashes.

## Install

1. Copy the contents of `SD/` into the root of the device's SD card, merging
   folders and keeping your other apps and data.
2. **RTL433 alone:** no firmware flash is required on the previous WirelessPi
   `2.0.0-pi11-wifite` release. That old name is a firmware revision, not a
   Raspberry Pi requirement.
3. **All cSploit Mini modules:** install the included firmware using
   `FLASHING.md`. Its ARP and TCP tools require the new firmware API. The FAP
   can load on the previous firmware and reports the missing extension.
4. Connect using the normal firmware Wi-Fi app before using cSploit Mini.
   Configure its target/name/reply settings explicitly before starting a test.

The existing WIFITE app and its SD data can remain installed. This package
adds the two new apps; it does not claim new WIFITE attack fixes.

## What was changed in the firmware

- Added a resident, optional network API for bounded TCP connection status
  and one-target packet reception/transmission used by cSploit Mini.
- Added callback/queue cleanup and restoration of normal Wi-Fi reception.
- Exported that API through the existing FAP symbol table.
- Updated the release version and made CMake track changes to its version
  header so the binary descriptor does not keep a stale revision label.

## Validation status

Both ESP32-S3 FAPs and the full firmware build. Icons are present, all FAP
imports resolve against the new and previous firmware, and the firmware fits
the existing app partition. Actual host tests decoded OOK/FSK fixtures and
checked pulse parsing, decoder behavior, DNS/LLMNR/NBT-NS packets, malformed
input, loopback worker responses, TCP scanning and secret discard. ARP relay
and restoration were exercised with a simulated packet backend.

**Hardware validation is still pending.** Live RF reception, available heap,
Wi-Fi driver callbacks, client ARP acceptance, DNS redirection and forwarding
throughput have not been verified on a physical T-Embed. This is a build for
controlled device testing, not a guarantee of production reliability. Host
sanitizer runs used AddressSanitizer/UBSan with leak detection disabled in the
test environment.

DNS redirection only affects matching queries that reach the device. Cached
addresses, encrypted DNS, network isolation and TLS certificate checks can
prevent the expected result. A local transmit counter is not proof of client
delivery. No HTTPS certificate bypass is included.

## Build from source

Extract `source/WirelessPi-Native-Tools-1.0-source.zip`.
Use ESP-IDF v5.4.1, commit
`4c2820d377d1375e787bcef612f0c32c1427d183`, with its submodules and ESP32-S3
toolchain installed. The external SDK/toolchain are not bundled. Keep the
project's dependency lockfile; ESP-IDF fetches its managed components.

In the ESP-IDF Python environment install `idf-component-manager==2.2.2`
and Pillow. Source the SDK's `export.sh`, then run from the extracted project:

```sh
bash BUILD-NATIVE-TOOLS.sh
```

This uses `sdkconfig.wifite` and the `lilygo_t_embed_cc1101` target. Outputs:
`build_native/furi_esp32.bin` and `build_native/fap/*.fap`.
The existing project includes SDK adapter/patch steps; see `BUILD-WIFITE.md`.

Host tests (Linux, C compiler with sanitizers):

```sh
bash applications_user/rtl433/tests/run.sh
bash applications_user/csploit_mini/tests/run.sh
```

All source licenses and upstream notices are preserved. RTL433 decoder
provenance is in `docs/RTL433-UPSTREAM.md`; the new cSploit Mini app and network
adapter retain their MIT notices. Existing firmware components keep their
original licenses.
