# Complete WirelessPi Native Tools SD apps

Download `WirelessPi-Native-Tools-Complete-SD.zip`, extract it, then copy the contents of its `SD` folder to your SD card root. Merge both `apps` and `apps_assets`. Do not put the enclosing `SD` folder on the card.

Includes WIFITE 0.8.1, RTL433 1.1.6, Wardriver 1.5.2, WDGWars Map 1.3, BW16 I2C 4.5, ProtoPirate 3.6.3 and the existing cSploit Mini 1.0. All 34 matching ProtoPirate companion plugins are included. No firmware reflash is needed when already running WirelessPi Native Tools 1.0. Static import compatibility was checked; physical-device behavior was not retested.

Individual FAP files are under `apps/`, with ProtoPirate plugins under `apps_assets/proto_pirate/plugins/`.

## ProtoPirate asset correction

The SD package now includes `apps_assets/proto_pirate/keystore/` and `models_db/`, previously omitted, alongside all 34 matching `pp_*.fal` plugins. These three data files match the existing published source archive byte for byte. Firmware and FAP binaries are unchanged. This corrects packaging; it is not a confirmed fix for every reported menu failure.

Copy both `apps/` and `apps_assets/` to the SD card root. Use `apps/Sub-GHz/proto_pirate.fap` from this release. If your card also has `apps/SubGhz/proto_pirate.fap`, back up that older copy outside the apps folder to avoid launching the wrong app. Legacy `protopirate_*_plugin.fal` files are not required by this release; use the supplied `pp_*.fal` set. Preserve your captures and settings.

The uploaded working-card archive contained duplicate ProtoPirate versions and older plugins; those duplicates were not added to this clean release. Both the main FAP and all 34 plugins were checked: 324 unique firmware imports, zero missing exports in the packaged firmware. Runtime behavior on affected devices remains unverified.
