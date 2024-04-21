import logging

from custom_components.dziunia.const import CURRENT
from custom_components.dziunia.const import VOLTAGE
from custom_components.dziunia.sensor import EmuCoordinator
from custom_components.dziunia.sensor import EmuCurrentSensor
from custom_components.dziunia.sensor import EmuVoltageSensor
from homeassistant.core import HomeAssistant


class Emu_1_40_V4_15val(EmuCoordinator):
    def __init__(
            self,
            hass: HomeAssistant,
            config_entry_id: str,
            logger: logging.Logger,
            sensor_id: int,
            serial_no: str,
            center_name: str,
            sensor_given_name: str,
    ) -> None:
        self._config_entry_id = config_entry_id
        self._hass = hass
        self._name = (
            sensor_given_name if sensor_given_name else f"{sensor_id}/{serial_no}"
        )
        self._sensor_id = sensor_id
        self._logger = logger
        self._serial_no = serial_no
        self._center_name = center_name
        self._config = dict(
            self._hass.config_entries.async_get_entry(self._config_entry_id).data
        )

        super().__init__(
            hass=hass,
            config_entry_id=config_entry_id,
            logger=logger,
            sensor_id=sensor_id,
            serial_no=serial_no,
            center_name=center_name,
            sensor_given_name=sensor_given_name,
        )
        self._sensors = [
            {
                "name": VOLTAGE,
                "position": 0,
                "has_scaling_factor": True,
                "unit_str": "V",
                "description_str": "Volts (vendor specific)",
                "sensor_class": EmuVoltageSensor,
            },
            {
                "name": CURRENT,
                "position": 1,
                "has_scaling_factor": True,
                "unit_str": "A",
                "description_str": "Ampere (vendor specific)",
                "sensor_class": EmuCurrentSensor,
            },
        ]

    @property
    def version_number(self) -> int:
        return 4

    @property
    def sensor_count(self) -> int:
        return 15

    @property
    def model_name(self) -> str:
        return "1/40"

    @property
    def manufacturer_name(self) -> str:
        return "EMU"