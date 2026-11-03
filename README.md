[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![Validate with HACS](https://img.shields.io/github/actions/workflow/status/barleybobs/homeassistant-ecowater-softener/validate-hacs.yml?label=Validate%20with%20HACS&style=for-the-badge)](https://github.com/barleybobs/homeassistant-ecowater-softener/actions)
[![Validate with Hassfest](https://img.shields.io/github/actions/workflow/status/barleybobs/homeassistant-ecowater-softener/validate-with-hassfest.yml?label=Validate%20with%20Hassfest&style=for-the-badge)](https://github.com/barleybobs/homeassistant-ecowater-softener/actions)

# **v4.0.0 BREAKING CHANGES**
**Entities have been removed and added in v4.0.0. You may have to remove your device from the integrations menu and re-add it.**

# Ecowater water softeners integration for Home Assistant

`ecowater_softener` is a _custom component_ for [Home Assistant](https://www.home-assistant.io/). The integration allows you to pull data from your Ecowater water softener.

## About this fork

This is a fork of [barleybobs/homeassistant-ecowater-softener](https://github.com/barleybobs/homeassistant-ecowater-softener) (v4.1.0). It uses the [kbzowski/ecowater-softener](https://github.com/kbzowski/ecowater-softener) library fork and adds:

| Entity | What it does |
|---|---|
| `sensor.<device>_next_recharge_time` | Timestamp of the next time the softener checks whether to recharge, taken from the recharge time set on the device. The softener only recharges then if it needs to. |
| `button.<device>_schedule_recharge` | Schedules a recharge for the next recharge time. |
| `button.<device>_recharge_now` | Starts a recharge immediately. Water is not softened while it runs (about 2 hours). |

`Last Recharge Date` no longer shows the day after the real recharge between midnight and midday.

The library is pinned to a commit of the fork in `manifest.json`. Home Assistant does not upgrade a package that is already installed, so when replacing the upstream integration, install the library once by hand and restart:

```bash
docker exec homeassistant uv pip install --system "ecowater-softener @ <URL from manifest.json>"
```

Install this fork through HACS as a custom repository (`https://github.com/kbzowski/homeassistant-ecowater-softener`, type Integration) or copy the folder manually as described below.

## Installation

#### HACS
1. Go to `HACS`
1. Search for `Ecowater Softener` and add it to HACS
1. Restart Home Assistant
1. Go to `Settings > Devices & Services`
1. Click `+ Add Integration`
1. Search for `Ecowater Softener` and follow the configuration instructions

#### Manually
Copy the `custom_components/ecowater_softener` folder into the config folder.

## Configuration
To add an Ecowater water softener, go to `Configuration > Integrations` in the UI. Then click the `+` button and from the list of integrations select Ecowater Softener. You will then be prompted to enter the username and password for your Ecowater account.

![Ecowater custom component login dialog](images/login.png)

After submitting your account login you will either be prompted to pick a device from your Ecowater account as shown below.

![Ecowater custom component device picker dialog](images/pick_device.png)

Or if you have already added all the devices in your Ecowater account you will recieve this error.

![Ecowater custom component all devices added error dialog](images/no_devices.png)

If the device is added successfully it should appear as shown.

![Device](images/devices.png)

This device will then have the entities show below.

![Entities](images/sensors.png)

## Changing Units

To change units select one of the entities and open the more info dialog and click the cog in the top right. This will bring up the settings for the entity. Then select `Unit of Measurement`, and a dropdown will appear where you can select the units you want.

![Entity more info settings dialog](images/change_units.png)


## Credits
- [Maxime Princelle](https://github.com/ThePrincelle) - French Translations
- [Bastian](https://github.com/Quotic) - German Translations
- [@figorr](https://github.com/figorr) - Updated deprecated constants & Updated to using `await async_forward_entry_setups` & Updated regex
- [Kyle Johnson](https://github.com/kylejohnson) - Discovering and documenting the Ecowater API
- [Matt Galloway](https://github.com/mattjgalloway) - Sorting manifest.json ordering
- [@Tazmanian79](https://github.com/Tazmanian79) - Updating state class from measurement to total
- [Tom Cassady](https://github.com/heytcass) - Grammar fixes
-   [@rewardone](https://github.com/rewardone) for creating [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) which is used to fetch the data
-   [Jeff Rescignano](https://github.com/JeffResc) for creating [sharkiq](https://github.com/JeffResc/sharkiq) which [ayla-iot-unofficial](https://github.com/rewardone/ayla-iot-unofficial) is based on.

## License
[MIT](https://choosealicense.com/licenses/mit/)
