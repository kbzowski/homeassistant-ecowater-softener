"""Recharge buttons for Ecowater softeners."""
from dataclasses import dataclass

import ecowater_softener

from homeassistant import config_entries
from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

@dataclass(frozen=True)
class EcowaterButtonEntityDescription(ButtonEntityDescription):
    """A class that describes button entities, key is the device method to call"""

BUTTON_TYPES: tuple[EcowaterButtonEntityDescription, ...] = (
    EcowaterButtonEntityDescription(
        key="schedule_recharge",
        name="Schedule Recharge",
        icon="mdi:calendar-refresh"
    ),
    EcowaterButtonEntityDescription(
        key="recharge_now",
        name="Recharge Now",
        icon="mdi:refresh"
    ),
)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: config_entries.ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the ecowater buttons."""
    config = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities(EcowaterButton(config, description) for description in BUTTON_TYPES)

class EcowaterButton(ButtonEntity):
    """Implementation of an ecowater recharge button."""

    _attr_has_entity_name = True
    entity_description: EcowaterButtonEntityDescription

    def __init__(self, config, description: EcowaterButtonEntityDescription) -> None:
        self.entity_description = description
        self._config = config
        self._serialnumber = config['device_serial_number']
        self._attr_unique_id = "ecowater_" + self._serialnumber.lower() + "_" + description.key
        # Name and model come from the sensor platform, which registers the device first
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, self._serialnumber)})

    def press(self) -> None:
        account = ecowater_softener.EcowaterAccount(self._config['username'], self._config['password'])
        device = next(device for device in account.get_devices() if device.serial_number == self._serialnumber)
        getattr(device, self.entity_description.key)()
